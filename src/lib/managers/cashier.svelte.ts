import { getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
import type { MenuItem, PaymentMethod } from '$lib/db/types';
import type { OrderEntry } from './cashier.types';

class CashierManager {
  currentOrder = $state<OrderEntry[]>([]);

  paymentMethod = $state<PaymentMethod | null>(null);
  customerName = $state<string>('');

  subtotal = $derived(this.currentOrder.reduce((sum, entry) => sum + entry.menuItem.price, 0));
  tax = $derived(this.subtotal * 0.07);
  total = $derived(this.subtotal + this.tax);
  isValidOrder = $derived(this.currentOrder.length > 0);

  async addToOrder(menuItem: MenuItem) {
    this.currentOrder.push({
      menuItem,
      ingredients: await getIngredientsForMenuItem(menuItem.id),
    });
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

  submit() {
    console.log(this.customerName);

    // Submit the order
    // TODO: Implement order submission logic
    this.clearOrder();
  }
}

// Persist CashierManager instance across HMRs
let cashierManager: CashierManager;

if (import.meta.hot) {
  if (!import.meta.hot.data.cashierManager) {
    import.meta.hot.data.cashierManager = new CashierManager();
  }
  cashierManager = import.meta.hot.data.cashierManager;
} else {
  cashierManager = new CashierManager();
}

export { cashierManager };
