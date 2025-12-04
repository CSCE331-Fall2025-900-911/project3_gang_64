import type { Employee } from '$lib/db/types';
import '@poppanator/sveltekit-svg/dist/svg.d.ts';

// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
declare global {
  namespace App {
    // interface Error {}
    interface Locals {
      employee: Employee?;
      translations: Record<string, Record<string, string>>;
    }
    interface PageData {
      employee: Employee?;
      translations: Record<string, Record<string, string>>;
    }
    // interface PageState {}
    // interface Platform {}
  }
}

declare module '@auth/sveltekit' {
  interface Session {
    employee?: Employee;
  }
}

declare module '@auth/core/jwt' {
  interface JWT {
    employee?: Employee;
  }
}

export {};
