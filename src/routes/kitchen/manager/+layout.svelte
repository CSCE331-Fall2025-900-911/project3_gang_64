<script lang="ts">
  import { localizeHref } from '$lib/i18n/runtime';
  import { t } from '$lib/utils/utils';
  import { AppShellSidebar, NavbarGroup, NavbarItem } from '@immich/ui';
  import {
    mdiAccount,
    mdiBadgeAccount,
    mdiChartBar,
    mdiCurrencyUsd,
    mdiFileDocument,
    mdiGauge,
    mdiPackageVariantClosed,
    mdiSilverware,
  } from '@mdi/js';

  let { children } = $props();
</script>

<div>
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    <NavbarItem href={localizeHref('/kitchen/manager/dashboard')} title={t('manager_dashboard')} icon={mdiGauge} />
    <NavbarItem
      href={localizeHref('/kitchen/manager/employees')}
      title={t('manager_employees')}
      icon={mdiBadgeAccount}
    />
    <NavbarGroup title="Sales" />
    <NavbarItem href={localizeHref('/kitchen/manager/orders')} title={t('manager_orders')} icon={mdiFileDocument} />
    <NavbarItem href={localizeHref('/kitchen/manager/customers')} title={t('manager_customers')} icon={mdiAccount} />
    <NavbarItem href={localizeHref('/kitchen/manager/reports')} title="Reports" icon={mdiCurrencyUsd} />
    <NavbarGroup title="Menu" />
    <NavbarItem
      href={localizeHref('/kitchen/manager/menu_items')}
      title={t('manager_menu_items')}
      icon={mdiSilverware}
    />
    <NavbarItem
      href={localizeHref('/kitchen/manager/inventory')}
      title={t('manager_inventory')}
      icon={mdiPackageVariantClosed}
    />
    <NavbarItem
      href={localizeHref('/kitchen/manager/usage_report')}
      title={t('manager_inventory_usage')}
      icon={mdiChartBar}
    />
  </AppShellSidebar>

  <div class="grow p-4">
    {@render children?.()}
  </div>
</div>
