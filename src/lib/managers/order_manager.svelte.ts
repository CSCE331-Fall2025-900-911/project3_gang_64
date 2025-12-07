import { createOrSelectCustomer } from '$lib/api/customer.remote';
import { getEmployees } from '$lib/api/employee.remote';
import { getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
import { submitOrder } from '$lib/api/orders.remote';
import { currentEmployee } from '$lib/auth/employee.svelte';
import type { Ingredient, MenuItem, PaymentMethod } from '$lib/db/types';
import { itemHash } from '$lib/utils/utils';
import type { OrderEntry } from './order_manager.types';

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
    itemIceLevel: 'None' | 'Less' | 'Normal' | 'Extra' = 'Normal',
    itemSugarLevel: 'None' | 'Less' | 'Normal' | 'Extra' = 'Normal',
    itemQuantity: number,
    itemIsCashier: boolean = false,
  ) {
    const baseItemIngredients = await getIngredientsForMenuItem(menuItem.id);

    if (!itemIngredients) {
      itemIngredients = baseItemIngredients;
    }

    const currentHash = itemHash(menuItem, itemIngredients, itemIceLevel, itemSugarLevel);

    const existing = this.currentOrder.find((entry) => {
      const existingHash = itemHash(entry.menuItem, entry.ingredients, entry.iceLevel, entry.sugarLevel);
      return existingHash === currentHash;
    });

    if (existing) {
      existing.quantity += itemQuantity;
      return;
    }

    if (!itemSubtotal) {
      itemSubtotal = menuItem.price;
    }

    itemIceLevel ??= 'Normal';
    itemSugarLevel ??= 'Normal';

    this.currentOrder.push({
      menuItem,
      ingredients: itemIngredients,
      quantity: itemQuantity,
      subtotal: itemSubtotal,
      iceLevel: itemIceLevel,
      sugarLevel: itemSugarLevel,
      isCashier: itemIsCashier,
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
    this.customerName = '';
    this.customerEmail = '';
  }

  async submit(isCashier: boolean) {
    // Create customer
    const customer = await createOrSelectCustomer({
      name: this.customerName,
      email: this.customerEmail,
    });

    const employee = isCashier ? (currentEmployee() ?? (await getEmployees())[0]) : null;

    // Submit the order
    await submitOrder({
      customerId: customer.id,
      paymentMethod: this.paymentMethod!,
      order: this.currentOrder,
      employeeId: employee?.id ?? null,
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
