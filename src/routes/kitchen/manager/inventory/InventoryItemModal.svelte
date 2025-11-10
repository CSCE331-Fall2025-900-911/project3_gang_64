<script lang="ts">
  import { createIngredient, updateIngredient } from '$lib/api/ingredient.remote';
  import { BlankIngredient, type CreateOrUpdate, type Ingredient, type NewIngredient } from '$lib/db/types';
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
      await createIngredient(item);
    } else {
      await updateIngredient({ id: mode.item.id, ...item });
    }

    onClose();
  }

  let item: NewIngredient = $state(mode.type === 'edit' ? mode.item : BlankIngredient);
  let submitting = $state(false);

  let valid = $derived(item.name.trim().length > 0 && item.currentStock >= 0 && item.orderStock >= 0);
</script>

<Modal title={mode.type === 'new' ? 'Create Ingredient' : 'Edit Ingredient'} icon={mdiPackage} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="Ingredient name" bind:value={item.name} />
      </Field>

      <Field label="Category">
        <Input placeholder="e.g., Vegetable, Dairy" bind:value={item.category} />
      </Field>

      <HStack gap={4}>
        <Field label="Current Stock">
          <NumberInput placeholder="0" bind:value={item.currentStock} />
        </Field>

        <Field label="Order Stock">
          <NumberInput placeholder="0" bind:value={item.orderStock} />
        </Field>
      </HStack>

      <Field label="Unit Price">
        <NumberInput placeholder="0" bind:value={item.unitPrice} />
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
