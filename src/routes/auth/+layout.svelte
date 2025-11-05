<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import { initializeTheme } from '@immich/ui';
  import '../../app.css';

  let { children } = $props();

  initializeTheme();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>ShareTea | Authentication</title>
</svelte:head>

{@render children?.()}
