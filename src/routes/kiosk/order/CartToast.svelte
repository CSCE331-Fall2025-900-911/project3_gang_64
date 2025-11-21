<script lang="ts">
  import { t } from '$lib/utils/utils';
  import { Button, modalManager, ToastContainer, ToastContent } from '@immich/ui';
  import { mdiCartOutline } from '@mdi/js';
  import CartModal from './CartModal.svelte';

  interface Props {
    onClose?: () => void;
    itemName: string;
  }

  const { onClose, itemName }: Props = $props();

  function onOpenCart() {
    modalManager.show(CartModal);
  }
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
      <Button color="primary" size="small" onclick={onOpenCart}>{t('cartToast_viewCart')}</Button>
    </div>
  </ToastContent>
</ToastContainer>
