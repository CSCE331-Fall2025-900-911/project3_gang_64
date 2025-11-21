import { createOrSelectCustomer } from '$lib/api/customer.remote';
import { getEmployees } from '$lib/api/employee.remote';
import { getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
import { submitOrder } from '$lib/api/orders.remote';
import type { Ingredient, MenuItem, PaymentMethod } from '$lib/db/types';
import type { OrderEntry } from './order_manager.types';

function itemHash(menuItem: MenuItem, ingredientIds: Ingredient[]): string {
  // Sort ingredient IDs to ensure consistent hash regardless of order
  const sortedIngredients = [...ingredientIds].sort((a, b) => a.id.localeCompare(b.id));
  return `${menuItem.id}-${sortedIngredients.map((i) => i.id).join(',')}`;
}

class OrderManager {
  currentOrder = $state<OrderEntry[]>([]);

  paymentMethod = $state<PaymentMethod | null>(null);
  customerName = $state<string>('');
  customerEmail = $state<string>('');

  subtotal = $derived(this.currentOrder.reduce((sum, entry) => sum + entry.subtotal * entry.quantity, 0));
  tax = $derived(this.subtotal * 0.07);
  total = $derived(this.subtotal + this.tax);
  isValidOrder = $derived(this.currentOrder.length > 0);

  async addToOrder(
    menuItem: MenuItem,
    itemIngredients: Ingredient[] | null = null,
    itemSubtotal: number | null = null,
    itemIceLevel: 'None' | 'Low' | 'Normal' | 'High' = 'Normal',
    itemSugarLevel: 'None' | 'Low' | 'Normal' | 'High' = 'Normal',
  ) {
    const baseItemIngredients = await getIngredientsForMenuItem(menuItem.id);

    if (!itemIngredients) {
      itemIngredients = baseItemIngredients;
    }

    const currentHash = itemHash(menuItem, itemIngredients);

    const existing = this.currentOrder.find((entry) => {
      const existingHash = itemHash(entry.menuItem, entry.ingredients);
      return existingHash === currentHash;
    });

    if (existing) {
      existing.quantity += 1;
      return;
    }

    if (!itemSubtotal) {
      itemSubtotal = menuItem.price;
    }

    const levelOptions = ['None', 'Low', 'Normal', 'High'] as const;

    if (!levelOptions.includes(itemIceLevel)) {
      itemIceLevel = 'Normal';
    }

    if (!levelOptions.includes(itemSugarLevel)) {
      itemSugarLevel = 'Normal';
    }

    this.currentOrder.push({
      menuItem,
      ingredients: itemIngredients,
      quantity: 1,
      subtotal: itemSubtotal,
      iceLevel: itemIceLevel,
      sugarLevel: itemSugarLevel,
    });
  }

  async duplicateOrderEntry(index: number) {
    this.currentOrder[index].quantity += 1;
  }

  getCurrentCartAmount(): number {
    return this.currentOrder.reduce((sum, entry) => sum + entry.quantity, 0);
  }

  modifyOrderEntry(index: number, newEntry: OrderEntry) {
    this.currentOrder[index] = newEntry;
  }

  removeFromOrder(index: number) {
    this.currentOrder.splice(index, 1);
  }

  clearOrder() {
    this.currentOrder = [];
    this.paymentMethod = null;
  }

  async submit() {
    // Create customer
    const customer = await createOrSelectCustomer({
      name: this.customerName,
      email: this.customerEmail,
    });

    // TODO: get employee ID from kitchen or kiosk session
    const employee = (await getEmployees())[0];

    // Submit the order
    await submitOrder({
      customerId: customer.id,
      paymentMethod: this.paymentMethod!,
      order: this.currentOrder,
      employeeId: employee.id,
    });

    this.clearOrder();
  }

  updateQuantity(index: number, newQuantity: number) {
    this.currentOrder[index].quantity = newQuantity;
  }
}

// Persist OrderManager instance across HMRs
let orderManager: OrderManager;

if (import.meta.hot) {
  if (!import.meta.hot.data.orderManager) {
    import.meta.hot.data.orderManager = new OrderManager();
  }
  orderManager = import.meta.hot.data.orderManager;
} else {
  orderManager = new OrderManager();
}

export { orderManager };
