import { getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
import type { MenuItem } from '$lib/db/types';
import type { OrderEntry } from './cashier.types';

class CashierManager {
  currentOrder = $state<OrderEntry[]>([]);

  subtotal = $derived.by(() => this.currentOrder.reduce((sum, entry) => sum + parseFloat(entry.menuItem.price), 0));
  tax = $derived.by(() => this.subtotal * 0.07);
  total = $derived.by(() => this.subtotal + this.tax);

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
