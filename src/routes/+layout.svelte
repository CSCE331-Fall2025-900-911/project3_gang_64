<script>
  import { page } from '$app/state';
  import { locales, localizeHref } from '$lib/i18n/runtime';
</script>

<slot></slot>

<div style="display:none">
  {#each locales as locale}
    <a href={localizeHref(page.url.pathname, { locale })}>{locale}</a>
  {/each}
</div>
