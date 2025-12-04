<script lang="ts">
  import { createIngredient, updateIngredient } from '$lib/api/ingredient.remote';
  import PriceInput from '$lib/components/PriceInput.svelte';
  import { BlankIngredient, type CreateOrUpdate, type Ingredient, type NewIngredient } from '$lib/db/types';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { td, generateNewTranslation, updateExistingTranslation } from '$lib/contexts/translations.svelte';
  import { Button, Field, Heading, HStack, Input, Modal, ModalBody, ModalFooter, NumberInput, Stack } from '@immich/ui';

  import { mdiPackage } from '@mdi/js';

  interface Props extends ModalProps {
    mode: CreateOrUpdate<Ingredient>;
  }

  let { onClose, mode }: Props = $props();

  async function submit() {
    submitting = true;

    if (mode.type === 'new') {
      item.name = await generateNewTranslation(itemName);
      item.category = await generateNewTranslation(categoryName);
      item.allergen = await Promise.all(
        allergenList.map(async (a) => {
          return await generateNewTranslation(a);
        }),
      );
      await createIngredient(item);
    } else {
      if (itemName !== originalItemName) {
        item.name = await updateExistingTranslation(item.name, itemName);
      }

      if (categoryName !== originalCategoryName) {
        item.category = await generateNewTranslation(categoryName);
      }

      if (allergenInput !== originalAllergenInput) {
        item.allergen = await Promise.all(
          allergenList.map(async (a) => {
            return await generateNewTranslation(a);
          }),
        );
      }

      await updateIngredient({ id: mode.item.id, ...item });
    }

    onClose();
  }

  let item: NewIngredient = $state(mode.type === 'edit' ? mode.item : BlankIngredient);
  let submitting = $state(false);

  // Store original values to detect changes
  const originalItemName = $derived(item.name ? td(item.name) : '');
  const originalCategoryName = $derived(item.category ? td(item.category) : '');
  const originalAllergenInput = $derived(
    Array.isArray(item.allergen) ? item.allergen.map((uuid) => td(uuid)).join(', ') : '',
  );

  let itemName = $state('');
  let categoryName = $state('');
  let allergenInput = $state('');

  $effect(() => {
    itemName = originalItemName;
    categoryName = originalCategoryName;
    allergenInput = originalAllergenInput;
  });

  let allergenList = $derived.by(() => {
    return allergenInput
      .split(',')
      .map((a) => a.trim())
      .filter((a) => a.length > 0);
  });

  let valid = $derived.by(() => {
    return (
      itemName.trim().length > 0 && categoryName.trim().length > 0 && item.currentStock >= 0 && item.orderStock >= 0
    );
  });
</script>

<Modal
  title={mode.type === 'new' ? t('manager_inventory_item_create_title') : t('manager_inventory_item_edit_title')}
  icon={mdiPackage}
  {onClose}
>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder={t('manager_inventory_item_placeholder_name')} bind:value={itemName} />
      </Field>

      <Field label="Category">
        <Input placeholder={t('manager_inventory_item_placeholder_category')} bind:value={categoryName} />
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
        <PriceInput placeholder={t('manager_inventory_item_placeholder_number')} bind:value={item.unitPrice} />
      </Field>

      <Heading size="small" class="mt-2">{t('manager_inventory_nutrition_section')}</Heading>

      <HStack gap={4}>
        <Field label={t('manager_inventory_item_label_calories')}>
          <NumberInput
            placeholder={t('manager_inventory_item_placeholder_number')}
            bind:value={item.calories}
            min={0}
          />
        </Field>

        <Field label={t('manager_inventory_item_label_fat')}>
          <NumberInput placeholder={t('manager_inventory_item_placeholder_number')} bind:value={item.fat_g} min={0} />
        </Field>
      </HStack>

      <HStack gap={4}>
        <Field label={t('manager_inventory_item_label_sodium')}>
          <NumberInput
            placeholder={t('manager_inventory_item_placeholder_number')}
            bind:value={item.sodium_g}
            min={0}
          />
        </Field>
        <Field label={t('manager_inventory_item_label_carbs')}>
          <NumberInput placeholder={t('manager_inventory_item_placeholder_number')} bind:value={item.carbs_g} min={0} />
        </Field>
      </HStack>

      <HStack gap={4}>
        <Field label={t('manager_inventory_item_label_sugar')}>
          <NumberInput placeholder={t('manager_inventory_item_placeholder_number')} bind:value={item.sugar_g} min={0} />
        </Field>
        <Field label={t('manager_inventory_item_label_caffeine')}>
          <NumberInput
            placeholder={t('manager_inventory_item_placeholder_number')}
            bind:value={item.caffiene_mg}
            min={0}
          />
        </Field>
      </HStack>
      <Field label={t('manager_inventory_item_label_allergens')}>
        <Input placeholder={t('manager_inventory_item_placeholder_allergens')} bind:value={allergenInput} />
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
