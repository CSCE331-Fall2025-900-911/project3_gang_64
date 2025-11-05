import type { Employee } from '$lib/db/types';
import '@poppanator/sveltekit-svg/dist/svg.d.ts';

// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
declare global {
  namespace App {
    // interface Error {}
    interface Locals {
      employee: Employee?;
    }
    interface PageData {
      employee: Employee?;
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
