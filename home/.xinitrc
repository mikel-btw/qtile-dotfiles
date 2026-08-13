export XDG_RUNTIME_DIR=/run/user/$(id -u)
mkdir -p $XDG_RUNTIME_DIR
chmod 700 $XDG_RUNTIME_DIR

eval $(dbus-launch --sh-syntax)
export DBUS_SESSION_BUS_ADDRESS

# Audio (PipeWire - WIP)
pipewire &
pipewire-pulse &
wireplumber &

exec qtile start
