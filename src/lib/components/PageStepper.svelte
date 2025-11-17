<script lang="ts">
  import { IconButton, Text } from '@immich/ui';
  import { mdiChevronLeft, mdiChevronRight } from '@mdi/js';
  import { t } from '$lib/utils/utils';

  interface Props {
    currentPage: number;
    totalPages: number;
  }

  let { currentPage = $bindable(), totalPages }: Props = $props();
</script>

<div class="flex items-center justify-center gap-2">
  <IconButton
    aria-label={t('pageStepper_previousPage')}
    icon={mdiChevronLeft}
    disabled={currentPage <= 1}
    onclick={() => currentPage--}
    size="small"
  />
  <Text size="large">{t('pageStepper_page')} {currentPage}/{totalPages}</Text>
  <IconButton
    aria-label={t('pageStepper_nextPage')}
    icon={mdiChevronRight}
    disabled={currentPage >= totalPages}
    onclick={() => currentPage++}
    size="small"
  />
</div>
