# qtile-dotfiles

Qtile desktop environment configuration for Void Linux.

## Hardware

- **CPU:** AMD Ryzen 3 3200U with Radeon Vega Mobile Gfx
- **GPU:** AMD/ATI Picasso/Raven 2 [Radeon Vega Series] (rev c4)
- **Driver:** xf86-video-amdgpu + mesa 26.1.6
- **Display:** X11 (startx)
- **Audio:** PipeWire 1.6.7 + WirePlumber 0.5.15

## System

- Void Linux + runit
- Kernel 6.18.42_1
- Qtile 0.36.0 / Python 3.14

## Structure

```
config/
  qtile/       -> ~/.config/qtile/
  kitty/       -> ~/.config/kitty/       (WIP)
home/
  .xinitrc     -> ~/.xinitrc
scripts/
  setup-aliases.sh
```

## Keybindings

### Windows

| Key | Action |
|-----|--------|
| `mod + h/j/k/l` | Move focus left/down/up/right |
| `mod + shift + h/j/k/l` | Move window left/down/up/right |
| `mod + ctrl + h/j/k/l` | Resize window |
| `mod + w` | Kill focused window |
| `mod + f` | Toggle fullscreen |
| `mod + t` | Toggle floating |
| `mod + space` | Focus next window |
| `mod + n` | Normalize window sizes |

### Apps

| Key | Action |
|-----|--------|
| `mod + Return` | Launch Kitty |
| `mod + r` | Launch Rofi |

### Layouts

| Key | Action |
|-----|--------|
| `mod + Tab` | Next layout |

### Workspaces

| Key | Action |
|-----|--------|
| `mod + 1-9` | Switch to group |
| `mod + shift + 1-9` | Move window to group |

### Media

| Key | Action |
|-----|--------|
| `XF86AudioRaiseVolume` | Volume +5% |
| `XF86AudioLowerVolume` | Volume -5% |
| `XF86MonBrightnessUp` | Brightness +10% |
| `XF86MonBrightnessDown` | Brightness -10% |

### Qtile

| Key | Action |
|-----|--------|
| `mod + ctrl + r` | Reload config |
| `mod + ctrl + q` | Shutdown Qtile |

## Status

| Component   | Status |
|-------------|--------|
| Qtile       | working |
| X11/startx  | working |
| PulseAudio  | working |
| Rofi        | installed, not configured |
| Brightness  | working (brightnessctl, group video) |
| Fonts       | JetBrains Mono installed manually |

## Dependencies

```
rofi
python3-psutil
brightnessctl
pulseaudio
curl
unzip
```

## Notes

- `/run/user/1000` must exist before starting X. Created manually with root.
- User must be in `video` group for brightnessctl without sudo.
- JetBrains Mono installed to `~/.local/share/fonts/` (not in Void repos).

