<script lang="ts">
	import { getEmployees } from '$lib/api/test.remote';
</script>

<ul>
	{#each await getEmployees() as { username, id }}
		<li><a href="/employee/{id}">{username}</a></li>
	{/each}
</ul>

<button onclick={() => getEmployees().refresh()}> Check for new posts </button>
