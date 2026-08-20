export XDG_RUNTIME_DIR=/run/user/$(id -u)
mkdir -p $XDG_RUNTIME_DIR
chmod 700 $XDG_RUNTIME_DIR

eval $(dbus-launch --sh-syntax)
export DBUS_SESSION_BUS_ADDRESS

pulseaudio --start

setxkbmap latam

xrandr --output HDMI-A-0 --mode 1920x1080 --rate 60 --above eDP 2>/dev/null

picom --config ~/.config/picom/picom.conf &

nitrogen --restore &

exec qtile start
