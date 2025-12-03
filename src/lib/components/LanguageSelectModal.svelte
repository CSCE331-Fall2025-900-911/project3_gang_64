<script lang="ts">
  import { t, type ModalProps } from '$lib/utils/utils';
  import { Modal, ModalBody, Select, type SelectItem } from '@immich/ui';
  import { mdiTranslate } from '@mdi/js';
  import { locales, setLocale, getLocale, type Locale } from '$lib/i18n/runtime';

  let { onClose }: ModalProps = $props();

  const languages: SelectItem[] = locales.map((locale) => {
    try {
      const displayNames = new Intl.DisplayNames([locale], { type: 'language' });
      const label = displayNames.of(locale) || locale;
      return { label: label.charAt(0).toUpperCase() + label.slice(1), value: locale };
    } catch {
      return { label: locale.toUpperCase(), value: locale };
    }
  });

  let selectedLanguage = $state<SelectItem>(languages.find((lang) => lang.value === getLocale()) ?? languages[0]);

  function handleLanguageChange(selected: SelectItem) {
    setLocale(selected.value as Locale);
  }
</script>

<Modal title={t('change_language_label')} size="small" {onClose} icon={mdiTranslate}>
  <ModalBody>
    <Select data={languages} onChange={handleLanguageChange} bind:value={selectedLanguage} />
  </ModalBody>
</Modal>
