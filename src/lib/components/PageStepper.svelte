<script lang="ts">
  import { IconButton, Text } from '@immich/ui';
  import { mdiChevronLeft, mdiChevronRight } from '@mdi/js';

  interface Props {
    currentPage: number;
    totalPages: number;
  }

  let { currentPage = $bindable(), totalPages }: Props = $props();
</script>

<div class="flex items-center justify-center gap-2">
  <IconButton
    aria-label="Previous Page"
    icon={mdiChevronLeft}
    disabled={currentPage <= 1}
    onclick={() => currentPage--}
    size="small"
  />
  <Text size="large">Page {currentPage}/{totalPages}</Text>
  <IconButton
    aria-label="Next Page"
    icon={mdiChevronRight}
    disabled={currentPage >= totalPages}
    onclick={() => currentPage++}
    size="small"
  />
</div>
