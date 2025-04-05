read -p "Give the path for the working folder on the VS code: " path

cd /

sudo dbus-launch  flatpak run com.visualstudio.code --no-sandbox --new-window "$path"
