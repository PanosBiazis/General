#!/bin/bash

read -p "Give the path for the working folder on VS Code: " path

# Expand `~` if the user provides a home directory path
path=$(eval echo "$path")

# Ensure the path exists
if [ -d "$path" ]; then
    flatpak run com.visualstudio.code --no-sandbox --new-window "$path"
else
    echo "Error: Directory does not exist!"
fi
#read -p "Give the path for the working folder on the VS code: " path

#cd /

#sudo dbus-launch  flatpak run com.visualstudio.code --no-sandbox --new-window "$path"
