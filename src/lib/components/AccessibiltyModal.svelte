<script lang="ts">
  import { accessibilityManager, type ColorblindMode } from '$lib/managers/accessibility.svelte';
  import { t, type ModalProps } from '$lib/utils/utils';
  import {
    Button,
    Field,
    HStack,
    Label,
    Modal,
    ModalBody,
    Select,
    Stack,
    theme,
    toggleTheme,
    type SelectItem,
  } from '@immich/ui';
  import { mdiMoonWaningCrescent, mdiWeatherSunny, mdiWheelchair } from '@mdi/js';

  let { onClose }: ModalProps = $props();

  const selectorModes: SelectItem[] = [
    { label: 'Off', value: 'off' },
    { label: 'Protanopia', value: 'protanopia' },
    { label: 'Deuteranopia', value: 'deuteranopia' },
    { label: 'Tritanopia', value: 'tritanopia' },
  ];

  function onModeChange(selected: SelectItem) {
    console.log('Selected mode:', selected.value);
    accessibilityManager.setColorblindMode(selected.value as ColorblindMode);
  }

  let selectedMode = $derived(
    selectorModes.find((item) => {
      if (accessibilityManager.colorblindMode === 'normal') {
        return item.value === 'off';
      } else {
        return item.value === accessibilityManager.colorblindMode;
      }
    }) ?? selectorModes[0],
  );
</script>

<Modal title={t('accessibility_options_label')} size="small" {onClose} icon={mdiWheelchair}>
  <ModalBody>
    <Stack gap={4}>
      <Stack>
        <Label>{t('colorblind_mode_label')}</Label>
        <HStack>
          <Button
            leadingIcon={mdiWeatherSunny}
            class="w-1/2"
            color={theme.value == 'light' ? 'primary' : 'secondary'}
            onclick={() => (theme.value != 'light' ? toggleTheme() : null)}
          >
            {t('light_mode_label')}
          </Button>
          <Button
            leadingIcon={mdiMoonWaningCrescent}
            class="w-1/2"
            color={theme.value == 'dark' ? 'primary' : 'secondary'}
            onclick={() => (theme.value != 'dark' ? toggleTheme() : null)}
          >
            {t('dark_mode_label')}
          </Button>
        </HStack>
      </Stack>
      <Field label={t('colorblind_mode_label')}>
        <Select data={selectorModes} onChange={onModeChange} bind:value={selectedMode} />
      </Field>
    </Stack>
  </ModalBody>
</Modal>
