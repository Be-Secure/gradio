import { test, describe, assert, afterEach } from "vitest";
import { cleanup, render } from "@gradio/tootils";
import Chatbot from "./index.svelte";
import type { LoadingStatus } from "@gradio/statustracker/types";
import type { FileData } from "@gradio/upload";

const loading_status: LoadingStatus = {
	eta: 0,
	queue_position: 1,
	queue_size: 1,
	status: "complete",
	scroll_to_output: false,
	visible: true,
	fn_index: 0,
	show_progress: "full"
};

describe("Chatbot", () => {
	afterEach(() => cleanup());

	test("renders user and bot messages", async () => {
		const { getAllByTestId } = await render(Chatbot, {
			loading_status,
			label: "chatbot",
			value: [["user message one", "bot message one"]],
			root: "",
			root_url: "",
			latex_delimiters: [{ left: "$$", right: "$$", display: true }],
			theme_mode: "dark"
		});

		const bot = getAllByTestId("user")[0];
		const user = getAllByTestId("bot")[0];

		assert.exists(bot);
		assert.exists(user);
	});

	test("renders additional message as they are passed", async () => {
		const { component, getAllByTestId } = await render(Chatbot, {
			loading_status,
			label: "chatbot",
			value: [["user message one", "bot message one"]],
			root: "",
			root_url: "",
			latex_delimiters: [{ left: "$$", right: "$$", display: true }],
			theme_mode: "dark"
		});

		await component.$set({
			value: [
				["user message one", "bot message one"],
				["user message two", "bot message two"]
			]
		});

		const user_2 = getAllByTestId("user");
		const bot_2 = getAllByTestId("bot");

		assert.equal(user_2.length, 2);
		assert.equal(bot_2.length, 2);

		assert.exists(user_2[1]);
		assert.exists(bot_2[1]);
	});

	test("renders image bot and user messages", async () => {
		const { component, getAllByTestId } = await render(Chatbot, {
			loading_status,
			label: "chatbot",
			value: undefined,
			root: "",
			root_url: "",
			latex_delimiters: [],
			theme_mode: "dark"
		});

		let value: [string | FileData | null, string | FileData | null][] = Array(
			2
		).fill([
			{
				name: "https://gradio-builds.s3.amazonaws.com/demo-files/cheetah1.jpg",
				mime_type: "image/jpeg",
				alt_text: null,
				data: null,
				is_file: true
			}
		]);

		await component.$set({
			value: value
		});

		const image = getAllByTestId("chatbot-image") as HTMLImageElement[];
		assert.isTrue(image[0].src.includes("cheetah1.jpg"));
		assert.isTrue(image[1].src.includes("cheetah1.jpg"));
	});

	test("renders video bot and user messages", async () => {
		const { component, getAllByTestId } = await render(Chatbot, {
			loading_status,
			label: "chatbot",
			root: "",
			root_url: "",
			latex_delimiters: [],
			theme_mode: "dark"
		});
		let value: Array<[string | FileData | null, string | FileData | null]> =
			Array(2).fill([
				{
					name: "https://gradio-builds.s3.amazonaws.com/demo-files/video_sample.mp4",
					mime_type: "video/mp4",
					alt_text: null,
					data: null,
					is_file: true
				}
			]);
		await component.$set({
			value: value
		});

		const video = getAllByTestId("chatbot-video") as HTMLVideoElement[];
		assert.isTrue(video[0].src.includes("video_sample.mp4"));
		assert.isTrue(video[1].src.includes("video_sample.mp4"));
	});

	test("renders audio bot and user messages", async () => {
		const { component, getAllByTestId } = await render(Chatbot, {
			loading_status,
			label: "chatbot",
			root: "",
			root_url: "",
			latex_delimiters: [],
			theme_mode: "dark"
		});

		let value = Array(2).fill([
			{
				name: "https://gradio-builds.s3.amazonaws.com/demo-files/audio_sample.wav",
				mime_type: "audio/wav",
				alt_text: null,
				data: null,
				is_file: true
			}
		]);

		await component.$set({
			value: value
		});

		const audio = getAllByTestId("chatbot-audio") as HTMLAudioElement[];
		assert.isTrue(audio[0].src.includes("audio_sample.wav"));
		assert.isTrue(audio[1].src.includes("audio_sample.wav"));
	});

	test("renders hyperlinks to file bot and user messages", async () => {
		const { component, getAllByTestId } = await render(Chatbot, {
			loading_status,
			label: "chatbot",
			root: "",
			root_url: "",
			latex_delimiters: [],
			theme_mode: "dark"
		});

		let value = Array(2).fill([
			{
				name: "https://gradio-builds.s3.amazonaws.com/demo-files/titanic.csv",
				mime_type: "text/csv",
				alt_text: null,
				data: "https://gradio-builds.s3.amazonaws.com/demo-files/titanic.csv",
				is_file: true
			}
		]);

		await component.$set({
			value: value
		});

		const file_link = getAllByTestId("chatbot-file") as HTMLAnchorElement[];
		assert.isTrue(file_link[0].href.includes("titanic.csv"));
		assert.isTrue(file_link[0].href.includes("titanic.csv"));
	});
});
