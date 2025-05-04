#!/bin/sh

# Requires inotify-tools (sudo pacman -S inotify-tools)
# Automatically runs `build.sh` every time the filesystem changes

ROOT=$(dirname $0)

# Args:
# -m: "monitor mode", continue to wait for fs events instead of exiting after
# the first one
# -r: monitor directories recursively
# -e close_write: watch for files being closed after being opened in write mode
# -e delete: watch for deleted files
# --exclude $ROOT/builder/target: don't watch the builder/target folder - this
#   is the Rust build folder, if we watched this there'd be an infinite loop
#   because building would create new files there which would then trigger
#   another build.
# $ROOT: watch all files in this repo
inotifywait -m -e close_write -e delete --exclude site/* $ROOT |
    while read path action file; do
        clear
        python3 build.py
    done
