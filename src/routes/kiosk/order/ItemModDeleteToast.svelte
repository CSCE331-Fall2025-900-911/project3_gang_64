<script lang="ts">
  import { t } from '$lib/utils/utils';
  import { ToastContainer, ToastContent } from '@immich/ui';
  import { mdiCartOutline } from '@mdi/js';

  interface Props {
    onClose?: () => void;
  }

  const { onClose }: Props = $props();
</script>

<ToastContainer color="primary">
  <ToastContent
    icon={mdiCartOutline}
    color="danger"
    title={t('itemModDeleteToast_title')}
    description={t('itemModDeleteToast_description')}
    {onClose}
  ></ToastContent>
</ToastContainer>
