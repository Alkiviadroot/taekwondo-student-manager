<script lang="ts">
	// Most of your app wide CSS should be put in this file
	import '../app.postcss';
	//Floating UI (Popup)
	import { computePosition, autoUpdate, offset, shift, flip, arrow } from '@floating-ui/dom';
	import { storePopup } from '@skeletonlabs/skeleton';
	storePopup.set({ computePosition, autoUpdate, offset, shift, flip, arrow });
	// Fluent
	import 'fluent-svelte/theme.css';
	
	// Initialize Stores
	import { initializeStores } from '@skeletonlabs/skeleton';
	initializeStores();
</script>

<slot />
