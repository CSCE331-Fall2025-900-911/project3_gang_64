<script lang="ts">
  import { t } from '$lib/utils/utils';
  import { Button, ToastContainer, ToastContent } from '@immich/ui';
  import { mdiCartOutline } from '@mdi/js';

  interface Props {
    onClose?: () => void;
    itemName: string;
  }

  const { onClose, itemName }: Props = $props();
</script>

<ToastContainer color="primary">
  <ToastContent
    icon={mdiCartOutline}
    color="primary"
    title={t('cartToast_title')}
    description={t('cartToast_description', { item_name: itemName })}
    {onClose}
  >
    <div class="flex justify-end gap-2 px-2 pb-2">
      <Button href="/kiosk/cart" color="primary" size="small">{t('cartToast_viewCart')}</Button>
    </div>
  </ToastContent>
</ToastContainer>
