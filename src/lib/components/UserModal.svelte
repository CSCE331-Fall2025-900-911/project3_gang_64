<script lang="ts">
  import { currentEmployee } from '$lib/auth/employee.svelte';
  import { signOut } from '@auth/sveltekit/client';
  import { Button, Modal, ModalBody } from '@immich/ui';

  interface Props {
    onClose: () => void;
  }

  let { onClose }: Props = $props();
  let employee = currentEmployee();
</script>

<Modal title={employee?.name} {onClose} icon={false} size="small">
  <ModalBody>
    <div>Email: {employee?.email}</div>
    <div>Role: {employee?.role}</div>

    <Button fullWidth color="danger" class="mt-4" onclick={() => signOut()}>Sign Out</Button>
  </ModalBody>
</Modal>
