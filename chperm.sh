#!/bin/bash


#echo -n "Give the path of the folder or file you want to change the permissions: "

#read path

#for i in {1..2}; do

#echo -n "Make the permissions for : "

#read perm

#if [perm -eq "everyone"  || "Everyone" || "EVERYONE"]
#then

#	sudo chmod -R 777 $path

#else 

#	echo "try again"
#	i=1
#fi 
 
#done


# Prompt the user for the target folder or file.
echo -n "Enter the path of the folder or file you want to change permissions for: "
read path

# Display a list of valid permission names and their corresponding chmod values.
echo "Choose one of the following permission sets:"
echo "  everyone  -> Full access for all (777)"
echo "  owner     -> Full access for owner only (700)"
echo "  group     -> Full access for owner and group (770)"
echo "  public    -> Owner full, group & others read and execute (755)"
echo "  read-only -> Read-only for everyone (444)"

attempts=0
while [ $attempts -lt 2 ]; do
    echo -n "Enter the permission name: "
    read perm

    case "$perm" in
        everyone|Everyone|EVERYONE)
            mode=777
            ;;
        owner|Owner|OWNER)
            mode=700
            ;;
        group|Group|GROUP)
            mode=770
            ;;
        public|Public|PUBLIC)
            mode=755
            ;;
        "read-only"|"Read-only"|"READ-ONLY")
            mode=444
            ;;
        *)
            echo "Invalid permission name. Valid options are: everyone, owner, group, public, read-only."
            attempts=$((attempts + 1))
            continue
            ;;
    esac

    # Change the permission recursively.
    sudo chmod -R $mode "$path"
    echo "Permissions for '$path' have been changed to $mode successfully."
    exit 0
done

echo "Failed to enter a valid permission name after 2 attempts."
