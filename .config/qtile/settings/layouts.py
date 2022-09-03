from libqtile import layout
from .colors import colors

theme = {
    "border_focus": colors["active"],
    "border_normal": colors["inactive"],
    "border_width": 1,
    "single_border_width": 0,
    "margin": 0,
}

layouts = [
    layout.MonadTall(**theme),
    layout.Max(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
    ]
)
