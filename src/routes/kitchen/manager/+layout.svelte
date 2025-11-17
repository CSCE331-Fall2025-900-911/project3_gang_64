<script lang="ts">
  import { AppShellSidebar, NavbarItem } from '@immich/ui';
  import { t } from '$lib/utils/utils';
  import {
    mdiAccount,
    mdiBadgeAccount,
    mdiFileDocument,
    mdiGauge,
    mdiPackageVariantClosed,
    mdiSilverware,
  } from '@mdi/js';

  let { children } = $props();
</script>

<div>
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    <NavbarItem href="/kitchen/manager/dashboard" title={t('manager_dashboard')} icon={mdiGauge} />
    <!-- TODO: Implement Reports -->
    <!-- <NavbarItem href="/kitchen/manager/reports" title="Reports" icon={mdiCurrencyUsd} /> -->
    <NavbarItem href="/kitchen/manager/employees" title={t('manager_employees')} icon={mdiBadgeAccount} />
    <NavbarItem href="/kitchen/manager/menu_items" title={t('manager_menu_items')} icon={mdiSilverware} />
    <NavbarItem href="/kitchen/manager/orders" title={t('manager_orders')} icon={mdiFileDocument} />
    <NavbarItem href="/kitchen/manager/customers" title={t('manager_customers')} icon={mdiAccount} />
    <NavbarItem href="/kitchen/manager/inventory" title={t('manager_inventory')} icon={mdiPackageVariantClosed} />
  </AppShellSidebar>

  <div class="grow p-4">
    {@render children?.()}
  </div>
</div>
