<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import Label from "./Label.svelte";
	import { LineChart as LabelIcon } from "@gradio/icons";
	import { Block, BlockLabel, Empty } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker/types";

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let color: undefined | string = undefined;
	export let value: {
		label?: string;
		confidences?: { label: string; confidence: number }[];
	} = {};
	export let label = "Label";
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let show_label = true;
	export let selectable = false;

	const dispatch = createEventDispatcher<{ change: undefined }>();

	$: ({ confidences, label: _label } = value);
	$: _label, confidences, dispatch("change");
</script>

<Block
	test_id="label"
	{visible}
	{elem_id}
	{elem_classes}
	{container}
	{scale}
	{min_width}
	padding={false}
>
	<StatusTracker {...loading_status} />
	{#if show_label}
		<BlockLabel Icon={LabelIcon} {label} disable={container === false} />
	{/if}
	{#if _label !== undefined && _label !== null}
		<Label on:select {selectable} {value} {color} />
	{:else}
		<Empty unpadded_box={true}><LabelIcon /></Empty>
	{/if}
</Block>
