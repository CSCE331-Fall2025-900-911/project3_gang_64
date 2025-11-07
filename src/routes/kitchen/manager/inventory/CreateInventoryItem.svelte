<script lang="ts">
  import { createIngredient } from '$lib/api/ingredient.remote';
  import { Button, Field, HStack, Input, Modal, ModalBody, ModalFooter, NumberInput, Stack } from '@immich/ui';
  import { mdiAccountPlus } from '@mdi/js';

  interface Props {
    onClose: () => void;
  }

  let { onClose }: Props = $props();

  async function submit() {
    submitting = true;

    await createIngredient({ name, currentStock, orderStock, unitPrice, category });
    onClose();
  }

  let name = $state('');
  let currentStock = $state(0);
  let orderStock = $state(0);
  let unitPrice = $state(0);
  let category = $state('');

  let submitting = $state(false);

  let valid = $derived(name.trim().length > 0 && currentStock >= 0 && orderStock >= 0);
</script>

<Modal title="Create Employee" icon={mdiAccountPlus} {onClose}>
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
      <Button onclick={submit} shape="round" color="primary" disabled={!valid} loading={submitting}>Create</Button>
    </div>
  </ModalFooter>
</Modal>
