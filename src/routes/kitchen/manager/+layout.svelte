<script lang="ts">
  import { AppShellSidebar, NavbarItem } from '@immich/ui';
  import {
    mdiAccount,
    mdiBadgeAccount,
    mdiCurrencyUsd,
    mdiFileDocument,
    mdiGauge,
    mdiPackageVariantClosed,
  } from '@mdi/js';

  let { children } = $props();
</script>

<div>
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    <NavbarItem href="/kitchen/manager/dashboard" title="Dashboard" icon={mdiGauge} />
    <NavbarItem href="/kitchen/manager/employees" title="Employees" icon={mdiBadgeAccount} />
    <NavbarItem href="/kitchen/manager/reports" title="Reports" icon={mdiCurrencyUsd} />
    <NavbarItem href="/kitchen/manager/orders" title="Orders" icon={mdiFileDocument} />
    <NavbarItem href="/kitchen/manager/customers" title="Customers" icon={mdiAccount} />
    <NavbarItem href="/kitchen/manager/inventory" title="Inventory" icon={mdiPackageVariantClosed} />
  </AppShellSidebar>

  <div class="grow p-4">
    {@render children?.()}
  </div>
</div>
