#!/bin/bash

# chmod +x ntfsf.sh

lsblk

# Check if /dev/sda1 exists
if lsblk | grep -q "/dev/sdb1"; then
    echo "/dev/sdb1 exists. Running ntfsfix..."
    sudo ntfsfix /dev/sdb1
    
    echo "Mounting /dev/sdb1 to ./local_media"
    sudo mount /dev/sdb1 ./local_media
else
    echo "/dev/sdb1 does not exist."
fi
