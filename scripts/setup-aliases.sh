#!/bin/bash
# Appends custom aliases to ~/.bashrc
# Safe to run multiple times - checks before inserting

MARKER="# qtile-dotfiles aliases"

if grep -q "$MARKER" ~/.bashrc; then
    echo "Aliases already present in ~/.bashrc, skipping."
    exit 0
fi

cat >> ~/.bashrc << 'EOF'

# qtile-dotfiles aliases
alias xi="sudo xbps-install"
alias xr="sudo xbps-remove"
alias xq="sudo xbps-query"
alias off="sudo poweroff"
alias rest="sudo reboot"
alias monitor="xrandr --output HDMI-A-0 --mode 1920x1080 --rate 60 --above eDP"
alias nomonitor="xrandr --output HDMI-A-0 --off"
EOF

echo "Aliases added to ~/.bashrc. Run 'source ~/.bashrc' to apply."
