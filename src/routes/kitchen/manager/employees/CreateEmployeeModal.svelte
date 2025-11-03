<script lang="ts">
  import { createEmployee } from '$lib/api/employee.remote';
  import { role } from '$lib/db/schema';
  import { titleCase } from '$lib/utils';
  import { Button, Field, Input, Modal, ModalBody, ModalFooter, PasswordInput, Select, Stack } from '@immich/ui';
  import { mdiAccountPlus } from '@mdi/js';

  interface Props {
    onClose: () => void;
  }

  let { onClose }: Props = $props();

  async function submit() {
    await createEmployee({ email, name, role: selectedRole.value });
    onClose();
  }

  let email = $state('');
  let name = $state('');

  const roleOptions = role.enumValues.map((r) => ({ label: titleCase(r), value: r }));
  let selectedRole = $state(roleOptions[0]);

  let valid = $derived.by(() => {
    return email.trim().length > 0 && name.trim().length >= 0;
  });
</script>

<Modal title="Create Employee" icon={mdiAccountPlus} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="John Doe" bind:value={name} />
      </Field>

      <Field label="Email">
        <PasswordInput placeholder="johndoe@example.com" bind:value={email} />
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
