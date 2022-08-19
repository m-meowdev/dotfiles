#!/bin/sh
~/.fehbg &
picom --experimental-backends &
qtile cmd-obj -o cmd -f reload_config & #fixes glitch where picom makes the qtile bar not appear on startup
dunst &
mpv --no-video ~/sounds/pokemonsfx/In-Battle\ Heal\ Status\ Refresh.mp3 &
