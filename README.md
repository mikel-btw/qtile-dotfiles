# qtile-dotfiles

Qtile desktop environment configuration for Void Linux.

## System

- Void Linux + runit
- X11 (startx)
- AMD Ryzen 3 3200U / Radeon Vega (amdgpu)
- Qtile 0.36.0 / Python 3.14

## Structure

```
config/
  qtile/       -> ~/.config/qtile/
  kitty/       -> ~/.config/kitty/       (WIP)
home/
  .xinitrc     -> ~/.xinitrc
```

## Status

| Component   | Status |
|-------------|--------|
| Qtile       | working |
| X11/startx  | working |
| PipeWire    | WIP |
| Rofi        | installed, not configured |
| Brightness  | working (brightnessctl, group video) |
| Fonts       | JetBrains Mono installed manually |

## Dependencies

```
rofi
python3-psutil
brightnessctl
pipewire
pipewire-pulse
wireplumber
curl
unzip
```

## Notes

- `/run/user/1000` must exist before starting X. Created manually with root.
- User must be in `video` group for brightnessctl without sudo.
- JetBrains Mono installed to `~/.local/share/fonts/` (not in Void repos).
