<script lang="ts">
  import { createEmployee, updateEmployee } from '$lib/api/employee.remote';
  import { role } from '$lib/db/schema';
  import type { CreateOrUpdate, Employee } from '$lib/db/types';
  import { titleCase } from '$lib/utils';
  import { Button, Field, Input, Modal, ModalBody, ModalFooter, Select, Stack } from '@immich/ui';
  import { mdiAccountPlus } from '@mdi/js';

  interface Props {
    onClose: () => void;
    mode: CreateOrUpdate<Employee>;
  }

  let { onClose, mode }: Props = $props();

  async function submit() {
    submitting = true;

    if (mode.type === 'new') {
      await createEmployee({ email, name, role: selectedRole.value });
    } else {
      await updateEmployee({ id: mode.item.id, email, name, role: selectedRole.value });
    }

    onClose();
  }

  let email = $state(mode.type === 'edit' ? mode.item.email : '');
  let name = $state(mode.type === 'edit' ? mode.item.name : '');
  let submitting = $state(false);

  const roleOptions = role.enumValues.map((r) => ({ label: titleCase(r), value: r }));
  let selectedRole = $state(
    mode.type === 'edit' ? roleOptions.find((r) => r.value === mode.item.role) || roleOptions[0] : roleOptions[0],
  );

  let valid = $derived(email.trim().length > 0 && name.trim().length >= 0 && email.includes('@'));
</script>

<Modal title={mode.type === 'new' ? 'Create Employee' : 'Edit Employee'} icon={mdiAccountPlus} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="John Doe" bind:value={name} />
      </Field>

      <Field label="Email">
        <Input placeholder="johndoe@example.com" bind:value={email} />
      </Field>

      <Field label="Role">
        <Select data={roleOptions} bind:value={selectedRole} />
      </Field>
    </Stack>
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={submit} shape="round" color="primary" disabled={!valid} loading={submitting}
        >{mode.type === 'new' ? 'Create' : 'Update'}</Button
      >
    </div>
  </ModalFooter>
</Modal>
