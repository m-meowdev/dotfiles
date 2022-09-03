# qtile config by m-meowdev
# https://github.com/m-meowdev/dotfiles

from os import path
import subprocess

from libqtile import hook

from settings.keys import keys
from settings.groups import groups, dgroups_key_binder
from settings.layouts import layouts, floating_layout
from settings.screens import screens


@hook.subscribe.startup_once
def autostart():
    home = path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])


dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
