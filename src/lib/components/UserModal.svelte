<script lang="ts">
  import { currentEmployee } from '$lib/auth/employee.svelte';
  import { m } from '$lib/i18n/messages';
  import { t, type ModalProps } from '$lib/utils/utils';
  import { signOut } from '@auth/sveltekit/client';
  import { Button, Modal, ModalBody } from '@immich/ui';

  let { onClose }: ModalProps = $props();
  let employee = currentEmployee();
</script>

<Modal title={employee?.name} {onClose} icon={false} size="small">
  <ModalBody>
    <div>{t('email')}: {employee?.email}</div>
    <div>{t('role')}: {t(employee!.role)}</div>

    <Button fullWidth color="danger" class="mt-4" onclick={() => signOut()}>{m.sign_out()}</Button>
  </ModalBody>
</Modal>
