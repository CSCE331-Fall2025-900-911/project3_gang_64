<script lang="ts">
  import { createIngredient, updateIngredient } from '$lib/api/ingredient.remote';
  import type { CreateOrUpdate, Ingredient } from '$lib/db/types';
  import { Button, Field, HStack, Input, Modal, ModalBody, ModalFooter, NumberInput, Stack } from '@immich/ui';
  import { mdiPackage } from '@mdi/js';

  interface Props {
    onClose: () => void;
    mode: CreateOrUpdate<Ingredient>;
  }

  let { onClose, mode }: Props = $props();

  async function submit() {
    submitting = true;

    if (mode.type === 'new') {
      await createIngredient({ name, currentStock, orderStock, unitPrice, category });
    } else {
      await updateIngredient({ id: mode.item.id, name, currentStock, orderStock, unitPrice, category });
    }

    onClose();
  }

  let name = $state(mode.type === 'edit' ? mode.item.name : '');
  let currentStock = $state(mode.type === 'edit' ? mode.item.currentStock : 0);
  let orderStock = $state(mode.type === 'edit' ? mode.item.orderStock : 0);
  let unitPrice = $state(mode.type === 'edit' ? mode.item.unitPrice : 0);
  let category = $state(mode.type === 'edit' ? mode.item.category : '');

  let submitting = $state(false);

  let valid = $derived(name.trim().length > 0 && currentStock >= 0 && orderStock >= 0);
</script>

<Modal title={mode.type === 'new' ? 'Create Ingredient' : 'Edit Ingredient'} icon={mdiPackage} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="Ingredient name" bind:value={name} />
      </Field>

      <Field label="Category">
        <Input placeholder="e.g., Vegetable, Dairy" bind:value={category} />
      </Field>

      <HStack gap={4}>
        <Field label="Current Stock">
          <NumberInput placeholder="0" bind:value={currentStock} />
        </Field>

        <Field label="Order Stock">
          <NumberInput placeholder="0" bind:value={orderStock} />
        </Field>
      </HStack>

      <Field label="Unit Price">
        <NumberInput placeholder="0" bind:value={unitPrice} />
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
