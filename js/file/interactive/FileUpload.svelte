<script lang="ts">
	import { createEventDispatcher, tick } from "svelte";
	import { Upload, ModifyUpload } from "@gradio/upload";
	import type { FileData } from "@gradio/upload";
	import { BlockLabel } from "@gradio/atoms";
	import { File } from "@gradio/icons";

	import { FilePreview } from "../shared";

	export let value: null | FileData | FileData[];

	export let label: string;
	export let show_label = true;
	export let file_count = "single";
	export let file_types: string[] | null = null;
	export let selectable = false;

	async function handle_upload({
		detail
	}: CustomEvent<FileData | FileData[]>): Promise<void> {
		value = detail;
		await tick();
		dispatch("change", value);
		dispatch("upload", detail);
	}

	function handle_clear({ detail }: CustomEvent<null>): void {
		value = null;
		dispatch("change", value);
		dispatch("clear");
	}

	const dispatch = createEventDispatcher<{
		change: FileData[] | FileData | null;
		clear: undefined;
		drag: boolean;
		upload: FileData[] | FileData;
		error: string;
	}>();

	let accept_file_types: string | null;
	if (file_types == null) {
		accept_file_types = null;
	} else {
		file_types = file_types.map((x) => {
			if (x.startsWith(".")) {
				return x;
			}
			return x + "/*";
		});
		accept_file_types = file_types.join(", ");
	}

	let dragging = false;
	$: dispatch("drag", dragging);
</script>

<BlockLabel
	{show_label}
	Icon={File}
	float={value === null}
	label={label || "File"}
/>

{#if value}
	<ModifyUpload on:clear={handle_clear} absolute />
	<FilePreview on:select {selectable} {value} />
{:else}
	<Upload
		on:load={handle_upload}
		filetype={accept_file_types}
		parse_to_data_url={false}
		{file_count}
		bind:dragging
	>
		<slot />
	</Upload>
{/if}
