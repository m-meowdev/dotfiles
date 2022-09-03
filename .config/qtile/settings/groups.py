from libqtile.config import Group
from libqtile.dgroups import simple_key_binder
from .keys import mod

groups = [
    Group(" DEV", layout="monadtall"),
    Group("爵 WEB", layout="monadtall"),
    Group(" ART", layout="monadtall"),
    Group(" DOC", layout="monadtall"),
    Group("辶 VID", layout="monadtall"),
    Group(" GAME", layout="monadtall"),
    Group(" MISC", layout="monadtall"),
]

dgroups_key_binder = simple_key_binder(mod)
