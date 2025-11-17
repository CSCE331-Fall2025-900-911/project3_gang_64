<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import { initializeTheme } from '@immich/ui';
  import '../../app.css';
  import { t } from '$lib/utils/utils';

  let { children } = $props();

  initializeTheme();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('authLayout_title')}</title>
</svelte:head>

{@render children?.()}
