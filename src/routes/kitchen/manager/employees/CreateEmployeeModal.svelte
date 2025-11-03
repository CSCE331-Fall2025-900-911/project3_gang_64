<script lang="ts">
  import { createEmployee } from '$lib/api/employee.remote';
  import { role } from '$lib/db/schema';
  import { titleCase } from '$lib/utils';
  import { Button, Field, Input, Modal, ModalBody, ModalFooter, PasswordInput, Select, Stack } from '@immich/ui';
  import { mdiAccountPlus } from '@mdi/js';
  import { v4 as uuidv4 } from 'uuid';

  interface Props {
    onClose: () => void;
  }

  let { onClose }: Props = $props();

  async function submit(event: Event) {
    await createEmployee({ id: uuidv4(), email, password, role: selectedRole.value });
    onClose();
  }

  let email = $state('');
  let password = $state('');

  const roleOptions = role.enumValues.map((r) => ({ label: titleCase(r), value: r }));
  let selectedRole = $state(roleOptions[0]);

  let valid = $derived.by(() => {
    return username.trim().length > 0 && password.trim().length >= 8;
  });
</script>

<Modal title="Create Employee" icon={mdiAccountPlus} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="John Doe" bind:value={username} />
      </Field>

      <Field label="Password">
        <PasswordInput placeholder="Enter password" bind:value={password} />
      </Field>

      <Field label="Role">
        <Select data={roleOptions} bind:value={selectedRole} />
      </Field>
    </Stack>
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={submit} shape="round" color="primary" disabled={!valid}>Create</Button>
    </div>
  </ModalFooter>
</Modal>
