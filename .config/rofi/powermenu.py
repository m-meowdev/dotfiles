#!/usr/bin/env python3

import os
import subprocess
import sys

options = {
    #"lock": "",
    "log out": "killall qtile",
    "shut down": "systemctl poweroff",
    "reboot": "systemctl reboot",
}

# print options
for x in options:
    print(x)

# check input
if os.getenv("ROFI_RETV") == "1":
    for x in options:
        if x == sys.argv[1]:
            subprocess.Popen(options[x].split(), stdout=subprocess.DEVNULL)
            
print("\0no-custom\x1ftrue")
