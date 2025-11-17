<script lang="ts">
  import { createIngredient, updateIngredient } from '$lib/api/ingredient.remote';
  import { BlankIngredient, type CreateOrUpdate, type Ingredient, type NewIngredient } from '$lib/db/types';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Field, HStack, Input, Modal, ModalBody, ModalFooter, NumberInput, Stack } from '@immich/ui';
  import { t } from '$lib/utils/utils';
  import { mdiPackage } from '@mdi/js';

  interface Props extends ModalProps {
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

<Modal
  title={mode.type === 'new' ? t('manager_inventory_item_create_title') : t('manager_inventory_item_edit_title')}
  icon={mdiPackage}
  {onClose}
>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder={t('manager_inventory_item_placeholder_name')} bind:value={item.name} />
      </Field>

      <Field label="Category">
        <Input placeholder={t('manager_inventory_item_placeholder_category')} bind:value={item.category} />
      </Field>

      <HStack gap={4}>
        <Field label={t('manager_inventory_item_label_current_stock')}>
          <NumberInput
            placeholder={t('manager_inventory_item_placeholder_number')}
            bind:value={item.currentStock}
            min={0}
          />
        </Field>

        <Field label={t('manager_inventory_item_label_order_stock')}>
          <NumberInput
            placeholder={t('manager_inventory_item_placeholder_number')}
            bind:value={item.orderStock}
            min={0}
          />
        </Field>
      </HStack>

      <Field label={t('manager_inventory_item_label_unit_price')}>
        <NumberInput placeholder={t('manager_inventory_item_placeholder_number')} bind:value={item.unitPrice} min={0} />
      </Field>
    </Stack>
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={submit} shape="round" color="primary" disabled={!valid} loading={submitting}
        >{mode.type === 'new' ? t('manager_inventory_item_create') : t('manager_inventory_item_update')}</Button
      >
    </div>
  </ModalFooter>
</Modal>
