<script lang="ts">
  import { t, type ModalProps } from '$lib/utils/utils';
  import { Button, Heading, Modal, ModalBody, ModalFooter, Stack } from '@immich/ui';
  import { mdiCheckboxMarked } from '@mdi/js';
  import { onMount } from 'svelte';

  interface Props extends ModalProps {
    title: string;
    description: string;
    number: string;
  }
  let { onClose, title, description, number }: Props = $props();

  onMount(() => {
    setTimeout(() => {
      onClose();
    }, 10000);
  });
</script>

<Modal {title} size="small" {onClose} icon={mdiCheckboxMarked}>
  <ModalBody>
    <Stack gap={4} align="center" class="text-center">
      <Heading size="medium">{description}</Heading>
      <p class="text-9xl font-bold">{number}</p>
    </Stack>
  </ModalBody>
  <ModalFooter>
    <Button fullWidth color="primary" onclick={onClose}>
      {t('common_close')}
    </Button>
  </ModalFooter>
</Modal>
