<script lang="ts">
  import { getEmployees } from '$lib/api/employee.remote';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { Employee } from '$lib/db/types';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { mdiMagnify, mdiPencil, mdiPlus } from '@mdi/js';
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
      title: 'Delete Employee',
      prompt: `Are you sure you want to delete ${employee.name}?`,
      confirmText: 'Delete',
      confirmColor: 'danger',
    });

    if (confirm) {
      // TODO: Handle deletion logic here
    }
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">Employees</Heading>
  <div class="flex w-1/3 items-center gap-2">
    <IconButton icon={mdiPlus} variant="filled" aria-label="Add Employee" style="p-4" onclick={showCreateModal} />
    <Input placeholder="Search" leadingIcon={mdiMagnify} bind:value={searchTerm} />
  </div>
</div>

{#if employees.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if employees.error}
  <p class="text-danger">Error loading employees: {employees.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-3/12">Name</TableHeaderCell>
      <TableHeaderCell width="w-4/12" align="left">Email</TableHeaderCell>
      <TableHeaderCell width="w-3/12">Role</TableHeaderCell>
      <TableHeaderCell width="w-2/12">Actions</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each searchedEmployees as employee}
        <TableRow>
          <TableCell width="w-3/12">{employee.name}</TableCell>
          <TableCell width="w-4/12" align="left">{employee.email}</TableCell>
          <TableCell width="w-3/12">{employee.role}</TableCell>
          <TableCell width="w-2/12" class="flex justify-center gap-2">
            <IconButton icon={mdiPencil} aria-label="Edit Employee" onclick={() => showEditModal(employee)} />
            <!-- <IconButton
              icon={mdiTrashCan}
              aria-label="Delete Employee"
              color="danger"
              onclick={() => showDeleteModal(employee)}
            /> -->
          </TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
{/if}
