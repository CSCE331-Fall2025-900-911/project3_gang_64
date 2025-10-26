<script lang="ts">
  import { getEmployees } from '$lib/api/employee.remote';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { mdiMagnify, mdiPlus } from '@mdi/js';
  import { cubicInOut } from 'svelte/easing';
  import { fade } from 'svelte/transition';
  import CreateEmployeeModal from './CreateEmployeeModal.svelte';

  let employees = getEmployees();
  let searchTerm = $state('');
  let searchedEmployees = $derived.by(() => {
    return employees.current?.filter((employee) => employee.username.includes(searchTerm));
  });

  function showCreateModal() {
    modalManager.show(CreateEmployeeModal);
  }
</script>

<div class="mb-6 flex items-center justify-between px-2">
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
  <table class="mt-4 w-full text-start">
    <thead class="mb-4 flex h-12 w-full rounded-md border bg-subtle">
      <tr class="flex w-full place-items-center text-center text-sm font-medium">
        <th class="w-3/12">ID</th>
        <th class="w-6/12 text-left">Username</th>
        <th class="w-3/12">Role</th>
      </tr>
    </thead>
    <tbody class="dark:border-immich-dark-gray block w-full overflow-y-auto rounded-md border">
      {#each searchedEmployees as employee}
        <tr
          transition:fade={{ duration: 400, easing: cubicInOut }}
          class="dark:text-immich-dark-fg flex w-full place-items-center py-2 text-center odd:bg-subtle/80 even:bg-subtle/20"
        >
          <td class="w-3/12">{employee.id}</td>
          <td class="w-6/12 text-left">{employee.username}</td>
          <td class="w-3/12">{employee.role}</td>
        </tr>
      {/each}
    </tbody>
  </table>
{/if}
