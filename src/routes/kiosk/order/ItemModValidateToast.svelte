<script lang="ts">
  import { t } from '$lib/utils/utils';
  import { ToastContainer, ToastContent } from '@immich/ui';
  import { mdiCartOutline } from '@mdi/js';

  interface Props {
    onClose?: () => void;
    isMax: boolean;
  }

  const { onClose, isMax }: Props = $props();
</script>

<ToastContainer color="primary">
  {#if isMax}
    <ToastContent
      icon={mdiCartOutline}
      color="warning"
      title={t('itemModAddToast_title')}
      description={t('itemModAddToast_description')}
      {onClose}
    ></ToastContent>
  {:else}
    <ToastContent
      icon={mdiCartOutline}
      color="warning"
      title={t('itemModDeleteToast_title')}
      description={t('itemModDeleteToast_description')}
      {onClose}
    ></ToastContent>
  {/if}
</ToastContainer>
