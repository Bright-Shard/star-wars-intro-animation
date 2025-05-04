# Star Wars Intro Animator

A web-based clone of the Star Wars movie intro.

![demo](resources/demo.gif)
![demo](resources/urmom.gif)

The animation is *highly* configurable, allowing you to change every piece of text and animation speeds. While the GIFs don't show it, it also plays the Star Wars intro music. The site also chunks text, so it can handle obscenely large text with no problems (I myself used it to animate over 727,000 lines of text - don't ask).

# Usage

1. In [`config.toml`](config.toml), set all of the text you want to appear and change any other settings you want. All the options are explained in the file.
2. Run [`build.py`](build.py).
3. Open [`site/index.html`](site/index.html) in your browser.

To see changes to `config.toml` in real-time, run `hot-reload.sh`. This requries a Linux host with `inotify-tools` installed.
