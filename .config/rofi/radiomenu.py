#!/usr/bin/env python3

import os
import subprocess
import sys

options = {
    "DKFM Shoegaze Radio": "https://kathy.torontocast.com:2005/stream",
    "Vocaloid Radio": "https://curiosity.shoutca.st/tunein/vocaloid.pls",
    "Naihatsu Radio": "http://listen.naihatsuradio.net/listen.pls",
}

# print options
for x in options:
    print(x)

# check input
if os.getenv("ROFI_RETV") == "1":
    for x in options:
        if x == sys.argv[1]:
            subprocess.Popen(["mpv", "--no-video", options[x]], stdout=subprocess.DEVNULL)
            
print("\0no-custom\x1ftrue")
