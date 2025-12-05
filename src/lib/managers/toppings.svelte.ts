import type { Ingredient } from '$lib/db/types';
import { getToppings } from '$lib/api/ingredient.remote';

class ToppingsManager {
  toppings = $state<Ingredient[]>([]);
  loaded = $state(false);

  async load() {
    if (this.loaded) return;

    const q = getToppings();
    $effect(() => {
      if (q.current && !this.loaded) {
        this.toppings = q.current;
        this.loaded = true;
      }
    });
  }
}

export const toppingsManager = new ToppingsManager();
