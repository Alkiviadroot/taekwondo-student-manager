<script lang="ts">
	import Deltia from '$lib/components/Forms/Deltia.svelte';
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<Deltia {data} />
