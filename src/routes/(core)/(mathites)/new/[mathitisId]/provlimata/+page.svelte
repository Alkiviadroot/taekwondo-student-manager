<script lang="ts">
	import Provlimata from '$lib/components/Forms/Provlimata.svelte';

	import type { PageData } from './$types';
	export let data: PageData;
</script>

<Provlimata {data} />
