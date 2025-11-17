<script lang="ts">
  import { deleteEmployee, getEmployees } from '$lib/api/employee.remote';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { Employee } from '$lib/db/types';
  import { t } from '$lib/utils/utils';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { mdiMagnify, mdiPencil, mdiPlus, mdiTrashCan } from '@mdi/js';
  import EmployeeModal from './EmployeeModal.svelte';

  let employees = getEmployees();
  let searchTerm = $state('');
  let searchedEmployees = $derived(
    employees.current?.filter(
      (employee) =>
        employee.email.toUpperCase().includes(searchTerm.toUpperCase()) ||
        employee.name.toUpperCase().includes(searchTerm.toUpperCase()),
    ) || [],
  );

  function showCreateModal() {
    modalManager.show(EmployeeModal, { mode: { type: 'new' } });
  }

  function showEditModal(employee: Employee) {
    modalManager.show(EmployeeModal, { mode: { type: 'edit', item: employee } });
  }

  async function showDeleteModal(employee: Employee) {
    const confirm = await modalManager.showDialog({
      title: t('manager_delete_employee_title'),
      prompt: `${t('manager_delete_employee_prompt')} ${employee.name}?`,
      confirmText: t('manager_delete_confirm_text'),
      confirmColor: 'danger',
      icon: mdiTrashCan,
    });

    if (confirm) {
      await deleteEmployee(employee.id);
    }
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">{t('manager_employees_title')}</Heading>
  <div class="flex w-1/3 items-center gap-2">
    <IconButton
      icon={mdiPlus}
      variant="filled"
      aria-label={t('manager_employees_add_aria')}
      style="p-4"
      onclick={showCreateModal}
    />
    <Input placeholder={t('manager_employees_search_placeholder')} leadingIcon={mdiMagnify} bind:value={searchTerm} />
  </div>
</div>

{#if employees.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if employees.error}
  <p class="text-danger">{t('manager_employees_error_loading')}: {employees.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-3/12">{t('manager_employees_table_name')}</TableHeaderCell>
      <TableHeaderCell width="w-4/12" align="left">{t('manager_employees_table_email')}</TableHeaderCell>
      <TableHeaderCell width="w-3/12">{t('manager_employees_table_role')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_employees_table_actions')}</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each searchedEmployees as employee}
        <TableRow>
          <TableCell width="w-3/12">{employee.name}</TableCell>
          <TableCell width="w-4/12" align="left">{employee.email}</TableCell>
          <TableCell width="w-3/12">{t(employee.role)}</TableCell>
          <TableCell width="w-2/12" class="flex justify-center gap-2">
            <IconButton
              icon={mdiPencil}
              aria-label={t('manager_employees_edit_aria')}
              onclick={() => showEditModal(employee)}
            />
            <IconButton
              icon={mdiTrashCan}
              aria-label={t('manager_employees_delete_aria')}
              color="danger"
              onclick={() => showDeleteModal(employee)}
            />
          </TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
{/if}
