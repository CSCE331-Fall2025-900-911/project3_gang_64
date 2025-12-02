<script lang="ts">
  import { initializeColorblindMode } from '$lib/managers/accessibility.svelte';
  import { onMount } from 'svelte';

  onMount(() => {
    initializeColorblindMode();
  });
</script>

<svg width="0" height="0" style="position: absolute">
  <filter id="normal">
    <feColorMatrix
      type="matrix"
      values="1 0 0 0 0
              0 1 0 0 0
              0 0 1 0 0
              0 0 0 1 0"
    />
  </filter>

  <filter id="protanopia">
    <feColorMatrix
      type="matrix"
      values="0.152 1.053 -0.205 0 0
              0.114 0.786 0.100 0 0
              -0.004 0.048 0.956 0 0
              0 0 0 1 0"
    />
  </filter>

  <filter id="deuteranopia">
    <feColorMatrix
      type="matrix"
      values="0.367 0.861 -0.228 0 0
              0.280 0.673 0.047 0 0
              -0.012 0.043 0.969 0 0
              0 0 0 1 0"
    />
  </filter>

  <filter id="tritanopia">
    <feColorMatrix
      type="matrix"
      values="1.255 -0.077 -0.178 0 0
          -0.078 0.930 0.148 0 0
           0.004 0.691 0.305 0 0
           0 0 0 1 0"
    />
  </filter>
</svg>
