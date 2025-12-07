<script>
  import { page } from '$app/state';
  import { setTranslations } from '$lib/contexts/translations.svelte';
  import { locales, localizeHref } from '$lib/i18n/runtime';
  import { initializeTheme } from '@immich/ui';
  import '../app.css';
  let { data, children } = $props();

  setTranslations(data.translations);

  initializeTheme();
</script>

{@render children()}

<div style="display:none">
  {#each locales as locale}
    <a href={localizeHref(page.url.pathname, { locale })}>{locale}</a>
  {/each}
</div>
