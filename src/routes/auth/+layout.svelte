<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import { t } from '$lib/utils/utils';

  let { children } = $props();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('authLayout_title')}</title>
</svelte:head>

{@render children?.()}
