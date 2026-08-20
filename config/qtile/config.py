import os
import subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"

# Colors
bg = "#0d0d0d"
fg = "#ffffff"
purple = "#7c3aed"
purple_dark = "#4c1d95"
gray = "#1a1a1a"

keys = [
    # Focus
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    # Move
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Resize
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),

    # Apps
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "r", lazy.spawn("rofi -show drun")),

    # Layouts
    Key([mod], "Tab", lazy.next_layout()),

    # Windows
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "t", lazy.window.toggle_floating()),

    # Qtile
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/volume-up.sh"))),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])

layouts = [
    layout.Columns(
        border_focus=purple,
        border_normal=gray,
        border_width=2,
        margin=10,
        border_on_single=True,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=13,
    padding=6,
    foreground=fg,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active=fg,
                    inactive="#555555",
                    highlight_method="block",
                    this_current_screen_border=purple,
                    block_highlight_text_color=fg,
                    borderwidth=2,
                    padding=6,
                ),
                widget.WindowName(
                    foreground=fg,
                ),
                widget.Spacer(),
                widget.CPU(
                    format="CPU {load_percent}%",
                    foreground=fg,
                ),
                widget.Sep(foreground=purple, padding=8),
                widget.Memory(
                    format="RAM {MemUsed:.0f}M",
                    foreground=fg,
                ),
                widget.Sep(foreground=purple, padding=8),
                widget.Volume(
                    fmt="VOL {}",
                    foreground=fg,
                ),
                widget.Sep(foreground=purple, padding=8),
                widget.Battery(
                    format="BAT {percent:2.0%}",
                    foreground=fg,
                    low_foreground="#ff5555",
                    low_percentage=0.2,
                ),
                widget.Sep(foreground=purple, padding=8),
                widget.Net(
                    format="NET {down:.1f}↓ {up:.1f}↑",
                    foreground=fg,
                ),
                widget.Sep(foreground=purple, padding=8),
                widget.Clock(
                    format="%d/%m/%Y %H:%M",
                    foreground=fg,
                ),
                widget.Sep(foreground=purple, padding=8),
                widget.Systray(),
            ],
            28,
            background=bg,
            margin=[0, 0, 0, 0],
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
