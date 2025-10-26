<script lang="ts">
  import { Modal, ModalBody } from '@immich/ui';

  interface Props {
    onClose: () => void;
  }

  let { onClose }: Props = $props();
</script>

<Modal title="User Information" {onClose} icon={false}>
  <ModalBody>
    <p>User details go here.</p>
  </ModalBody>
</Modal>
