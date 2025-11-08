<script lang="ts">
  import { Button, ToastContainer, ToastContent } from '@immich/ui';
  import { mdiCartOutline } from '@mdi/js';

  interface Props {
    onClose?: () => void;
  }

  const { onClose }: Props = $props();

  const cartUrl: string = '/kiosk/cart';
</script>

<ToastContainer color="primary">
  <ToastContent icon={mdiCartOutline} color="primary" title="Cart is Ready" description="Item added to order" {onClose}>
    <div class="flex justify-end gap-2 px-2 pb-2">
      <Button href={cartUrl} color="primary" size="small">View Cart</Button>
    </div>
  </ToastContent>
</ToastContainer>
