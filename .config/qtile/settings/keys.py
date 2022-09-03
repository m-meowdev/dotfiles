from libqtile.config import Key, KeyChord, Click, Drag
from libqtile.lazy import lazy

mod = "mod4"  # set mod to super/windows key
terminal = "alacritty"
web_browser = "qutebrowser"
launcher = "rofi"
scripts = {
    "run": " -show",
    "power": " -show power -config '~/.config/rofi/powermenu.rasi'",
    "radio": " -show radio -config '~/.config/rofi/radiomenu.rasi'",
    "theme": " -show theme -config '~/.config/rofi/thememenu.rasi'",
}

keys = [
    # window nav
    Key([mod], "h", lazy.layout.left(), desc="Move focus left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move focus to next window"),

    # move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # resize windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # kill windows
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    # switch layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Switch to next layout"),

    # reload and exit qtile
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload Qtile config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Exit Qtile"),

    # launch programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(web_browser), desc="Launch web browser"),
    KeyChord([mod], "r", [
        Key([], "r", lazy.spawn(launcher + scripts["run"])),
        Key([], "p", lazy.spawn(launcher + scripts["power"])),
        Key([], "l", lazy.spawn(launcher + scripts["radio"])),
        Key([], "t", lazy.spawn(launcher + scripts["theme"])),
    ]),

    # volume control
    # for vms and keyboards without volume keys (F1-3 is the location of the volume keys on my keyboard)
    Key([mod], "F3", lazy.spawn("amixer set Master 5%+"), desc="Increase volume"),
    Key([mod], "F2", lazy.spawn("amixer set Master 5%-"), desc="Decrease volume"),
    Key([mod], "F1", lazy.spawn("amixer set Master toggle"), desc="Toggle mute"),
    # for bare metal with volume keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+"), desc="Increase volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-"), desc="Decrease volume"),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="Toggle mute"),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
