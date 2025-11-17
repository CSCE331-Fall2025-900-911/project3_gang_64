<script lang="ts">
  import { Button, ToastContainer, ToastContent } from '@immich/ui';
  import { mdiCartOutline } from '@mdi/js';
  import { t } from '$lib/utils/utils';

  interface Props {
    onClose?: () => void;
  }

  const { onClose }: Props = $props();
</script>

<ToastContainer color="primary">
  <ToastContent
    icon={mdiCartOutline}
    color="primary"
    title={t('cartToast_title')}
    description={t('cartToast_description')}
    {onClose}
  >
    <div class="flex justify-end gap-2 px-2 pb-2">
      <Button href="/kiosk/cart" color="primary" size="small">{t('cartToast_viewCart')}</Button>
    </div>
  </ToastContent>
</ToastContainer>
