<script lang="ts">
  import { t } from '$lib/utils/utils';
  import { ToastContainer, ToastContent } from '@immich/ui';
  import { mdiPencil, mdiPencilOff } from '@mdi/js';

  interface Props {
    onClose?: () => void;
    isEdited: boolean;
  }

  const { onClose, isEdited }: Props = $props();
</script>

<ToastContainer color="primary">
  {#if isEdited}
    <ToastContent
      icon={mdiPencil}
      color="success"
      title={t('itemModEditSuccessToast_title')}
      description={t('itemModEditSuccessToast_description')}
      {onClose}
    ></ToastContent>
  {:else}
    <ToastContent
      icon={mdiPencilOff}
      color="warning"
      title={t('itemModEditFailToast_title')}
      description={t('itemModEditFailToast_description')}
      {onClose}
    ></ToastContent>
  {/if}
</ToastContainer>
