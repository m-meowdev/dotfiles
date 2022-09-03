# DISCLAIMER: multi-monitor support has not been tested

import subprocess
from libqtile.config import Screen
from libqtile import bar, widget
from .colors import colors

# get number of active monitors
monitors_cmd = subprocess.run("xrandr --listactivemonitors | wc -l", shell=True, stdout=subprocess.PIPE)
monitors = int(monitors_cmd.stdout) - 1

# index of primary monitor
primary_index = 0


# make bar with provided widgets
def make_bar(widgets):
    return bar.Bar(widgets, 24, background=colors["bar"], opacity=0.95)


# set widget font
widget_font = "TerminessTTF Nerd Font"

# widgets displayed on primary monitor
primary_widgets = [
    widget.TextBox(
        text="",
        font=widget_font,
        fontsize=20,
        padding=6,
        background=colors["color2"],
        foreground=colors["color1"],
    ),
    widget.GroupBox(
        font=widget_font,
        fontsize=14,
        highlight_method="block",
        this_current_screen_border=colors["color1"],
        block_highlight_text_color=colors["bar"],
        urgent_alert_method="block",
        borderwidth=0,
        rounded=False,
        disable_drag=True,
        padding=6,
        margin_x=0,
        active=colors["active"],
        inactive=colors["inactive"],
        background=colors["color2"],
    ),
    widget.Spacer(length=6),
    widget.WindowName(
        font=widget_font,
        fontsize=14,
        padding=6,
        foreground=colors["text"],
    ),
    widget.CheckUpdates(
        font=widget_font,
        fontsize=14,
        padding=6,
        colour_have_updates=colors["active"],
        background=colors["color2"],
        distro="Arch",
        display_format="{updates} ﮮ",
    ),
    widget.Clock(
        font=widget_font,
        fontsize=14,
        padding=6,
        format=" %a %m/%d/%Y |  %I:%M %p",
        background=colors["color1"],
        foreground=colors["bar"],
    ),
]

# widgets displayed on secondary monitors
secondary_widgets = primary_widgets[:-1]

# set screen on each monitor
screens = []
for x in range(monitors):
    if x == primary_index:
        screens.append(Screen(top=make_bar(primary_widgets)))
    else:
        screens.append(Screen(top=make_bar(secondary_widgets)))
