<script lang="ts">
  import { Icon, LoadingSpinner } from '@immich/ui';

  interface Props {
    title: string;
    value?: string | number;
    percentChange?: number;
    icon: string;
    iconBgColor?: string;
    iconColor?: string;
    bgColor?: string;
    loading?: boolean;
    error?: string;
  }

  let { title, value, percentChange, icon, loading = false, error }: Props = $props();

  let percentChangeColor = $derived(
    percentChange !== undefined
      ? percentChange >= 0
        ? 'text-green-600 dark:text-green-400'
        : 'text-red-600 dark:text-red-400'
      : '',
  );

  let percentChangeSign = $derived(percentChange !== undefined && percentChange >= 0 ? '+' : '');
</script>

<div class="w-1/3 rounded-xl border bg-subtle p-6">
  <div class="flex items-start justify-between">
    <div class="flex-1">
      <p class="text-sm font-medium text-gray-600 dark:text-gray-400">{title}</p>
      {#if loading}
        <div class="mt-2 flex items-center">
          <LoadingSpinner />
        </div>
      {:else if error}
        <p class="text-sm text-danger">{error}</p>
      {:else}
        <h2 class="mt-2 text-4xl font-bold text-gray-900 dark:text-gray-100">
          {value}
        </h2>
        {#if percentChange !== undefined}
          <p class="mt-2 text-xs {percentChangeColor}">
            {percentChangeSign}{percentChange.toFixed(2)}%
            <span class="text-gray-500">vs last week</span>
          </p>
        {/if}
      {/if}
    </div>
    <Icon {icon} size="28" class="text-gray-600 dark:text-gray-400" />
  </div>
</div>
