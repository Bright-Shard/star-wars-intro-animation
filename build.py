import tomllib

with open("site.html", "r") as template:
	with open("config.toml", "rb") as config:
		config = tomllib.load(config)

		javascript = f"""
		<script>
			const SCROLLING_TEXT = String.raw`{config["scrolling_text"].replace('`', '\\`')}`;
			const INTRO_PLACE = String.raw`{config["intro_place"]}`;
			const TITLE = String.raw`{config["title"]}`;

			const INTRO_FADE_IN_SPEED = {config["intro_fade_in_speed"]};
			const INTRO_FADE_OUT_SPEED = {config["intro_fade_out_speed"]};
			const INTRO_FADE_OUT_DELAY = {config["intro_fade_out_delay"]};
			const TITLE_DELAY = {config["title_delay"]};
			const LINES_PER_SECOND = {config["lps"]};

			const CHUNK_SIZE = {config["chunk_size"]};
			const SCROLLING_TEXT_HZ = {config["scrolling_text_hz"]};
		</script>
		"""

		template = template.read()
		out = template.replace("<head>", f"<head>{javascript}")
		with open("site/index.html", "w") as output:
			output.write(out)
		print("Finished")
