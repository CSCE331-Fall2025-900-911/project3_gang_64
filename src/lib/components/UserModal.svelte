<script lang="ts">
  import { currentEmployee } from '$lib/auth/employee.svelte';
  import type { ModalProps } from '$lib/utils';
  import { signOut } from '@auth/sveltekit/client';
  import { Button, Modal, ModalBody } from '@immich/ui';

  let { onClose }: ModalProps = $props();
  let employee = currentEmployee();
</script>

<Modal title={employee?.name} {onClose} icon={false} size="small">
  <ModalBody>
    <div>Email: {employee?.email}</div>
    <div>Role: {employee?.role}</div>

    <Button fullWidth color="danger" class="mt-4" onclick={() => signOut()}>Sign Out</Button>
  </ModalBody>
</Modal>
