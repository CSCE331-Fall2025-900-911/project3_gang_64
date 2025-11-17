<script lang="ts">
  import { fileUpload } from '$lib/utils/r2';
  import { Icon, IconButton, LoadingSpinner } from '@immich/ui';
  import { mdiImagePlus, mdiTrashCan } from '@mdi/js';

  interface Props {
    value?: string | null;
  }

  let { value = $bindable(null) }: Props = $props();

  let isDragging = $state(false);
  let previewUrl = $state<string | null>(value || null);
  let fileInput: HTMLInputElement;
  let uploading = $state(false);

  function handleDragOver(e: DragEvent) {
    e.preventDefault();
    isDragging = true;
  }

  function handleDragLeave(e: DragEvent) {
    e.preventDefault();
    isDragging = false;
  }

  function handleDrop(e: DragEvent) {
    e.preventDefault();
    isDragging = false;

    const files = e.dataTransfer?.files;
    if (files && files.length > 0) {
      const file = files[0];
      if (file.type.startsWith('image/')) {
        setFile(file);
      }
    }
  }

  function handleFileSelect(e: Event) {
    const target = e.target as HTMLInputElement;
    const files = target.files;
    if (files && files.length > 0) {
      setFile(files[0]);
    }
  }

  async function setFile(file: File) {
    uploading = true;

    // Create temporary preview URL
    const tempUrl = URL.createObjectURL(file);
    previewUrl = tempUrl;

    try {
      // Upload to R2 and get the URL
      const url = await fileUpload(file);

      // Replace preview with actual R2 URL
      URL.revokeObjectURL(tempUrl);
      previewUrl = url;
      value = url;
    } catch (error) {
      console.error('Failed to upload image:', error);
      URL.revokeObjectURL(tempUrl);
      previewUrl = null;
    } finally {
      uploading = false;
    }
  }

  function handleClick() {
    fileInput.click();
  }

  function clearImage() {
    value = null;
    previewUrl = null;
    fileInput.value = '';
  }
</script>

<div class="w-full">
  <input bind:this={fileInput} type="file" accept="image/*" onchange={handleFileSelect} class="hidden" />

  <div
    role="button"
    tabindex="0"
    class="relative flex h-36 w-full cursor-pointer items-center justify-center rounded-lg border-2 border-dashed transition-colors {isDragging
      ? 'border-primary bg-primary/10'
      : 'border-gray-300 hover:border-primary/50'}"
    ondragover={handleDragOver}
    ondragleave={handleDragLeave}
    ondrop={handleDrop}
    onclick={handleClick}
    onkeydown={(e) => e.key === 'Enter' && handleClick()}
  >
    {#if uploading}
      <div class="flex flex-col items-center gap-2">
        <LoadingSpinner size="large" />
        <p class="text-sm text-gray-600">Uploading...</p>
      </div>
    {:else if previewUrl}
      <div class="relative h-full w-full p-2">
        <img src={previewUrl} alt="Preview" class="h-full w-full object-contain" />
        <IconButton
          icon={mdiTrashCan}
          size="small"
          aria-label="Remove Image"
          color="danger"
          class="absolute top-2 right-2"
          onclick={(e: MouseEvent) => {
            e.stopPropagation();
            clearImage();
          }}
        />
      </div>
    {:else}
      <div class="flex flex-col justify-center text-center">
        <Icon icon={mdiImagePlus} size="48" class="mb-2 w-full text-gray-400" />
        <p class="mt-2 text-sm text-gray-600">
          <span class="font-semibold">Click to upload</span> or drag and drop
        </p>
        <p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
      </div>
    {/if}
  </div>
</div>
