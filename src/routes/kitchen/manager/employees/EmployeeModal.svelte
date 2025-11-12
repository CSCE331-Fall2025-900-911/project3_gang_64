<script lang="ts">
  import { createEmployee, updateEmployee } from '$lib/api/employee.remote';
  import { role } from '$lib/db/schema';
  import { BlankEmployee, type CreateOrUpdate, type Employee, type NewEmployee } from '$lib/db/types';
  import { titleCase, type ModalProps } from '$lib/utils';
  import { Button, Field, Input, Modal, ModalBody, ModalFooter, Select, Stack, type SelectItem } from '@immich/ui';
  import { mdiAccountPlus } from '@mdi/js';

  interface Props extends ModalProps {
    mode: CreateOrUpdate<Employee>;
  }

  let { onClose, mode }: Props = $props();

  async function submit() {
    submitting = true;

    if (mode.type === 'new') {
      await createEmployee(employee);
    } else {
      await updateEmployee({ id: mode.item.id, ...employee });
    }

    onClose();
  }

  let employee: NewEmployee = $state(mode.type === 'edit' ? mode.item : BlankEmployee);
  let submitting = $state(false);

  const roleOptions = role.enumValues.map((r) => ({ label: titleCase(r), value: r }));
  let selectedRole: SelectItem = $derived(
    roleOptions.find((option) => option.value === employee.role) || roleOptions[0],
  );

  let valid = $derived(
    employee.email.trim().length > 0 && employee.name.trim().length >= 0 && employee.email.includes('@'),
  );

  function updateRole(selected: SelectItem) {
    employee.role = selected.value as Employee['role'];
  }
</script>

<Modal title={mode.type === 'new' ? 'Create Employee' : 'Edit Employee'} icon={mdiAccountPlus} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="John Doe" bind:value={employee.name} />
      </Field>

      <Field label="Email">
        <Input placeholder="johndoe@example.com" bind:value={employee.email} />
      </Field>

      <Field label="Role">
        <Select data={roleOptions} bind:value={selectedRole} onChange={updateRole} />
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
