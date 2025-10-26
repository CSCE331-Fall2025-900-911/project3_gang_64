<script lang="ts">
  import { AppShellSidebar, NavbarItem } from '@immich/ui';
  import { mdiAccount, mdiCurrencyUsd, mdiGauge } from '@mdi/js';

  let { children } = $props();
</script>

<div>
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    <NavbarItem href="/kitchen/manager/dashboard" title="Dashboard" icon={mdiGauge} />
    <NavbarItem href="/kitchen/manager/employees" title="Employees" icon={mdiAccount} />
    <NavbarItem href="/kitchen/manager/reports" title="Reports" icon={mdiCurrencyUsd} />
  </AppShellSidebar>

  <div class="grow p-4">
    {@render children?.()}
  </div>
</div>
