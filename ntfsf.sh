#!/bin/bash

# chmod +x ntfsf.sh

lsblk

# Check if /dev/sda1 exists
if lsblk | grep -q "/dev/sdb1"; then
    echo "/dev/sdb1 exists. Running ntfsfix..."
    sudo ntfsfix /dev/sdb1
    
    echo "Mounting /dev/sdb1 to /media/panos..."
    sudo mount /dev/sdb1 /media/panos
else
    echo "/dev/sdb1 does not exist."
fi
