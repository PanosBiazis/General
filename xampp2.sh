cd /

cd /opt/lampp

#sudo systemctl start httpd

#sudo systemctl start mariadb

#sudo systemctl status httpd

#sudo systemctl status mariadb

#sudo /opt/lampp/lampp start

#if [sudo /opt/lampp/lampp start -eq false || FALSE]; then

#	#echo "Error!!!\nRestarting again!!!\n"

#	sudo /opt/lampp/lampp status

#	sudo /opt/lampp/lampp restart


#	if [sudo /opt/lampp/lampp start -eq false || FALSE]; then

#        #echo "Error!!!"

#        sudo /opt/lampp/lampp status

	
#	fi


#fi





sudo ./manager-linux-x64.run

#This file  has been created by Panos Biazis to open xampp

#!/bin/bash

cd /opt/lampp || exit 1  # Exit if the directory does not exist

# Start XAMPP
#sudo /opt/lampp/lampp start

# Check if XAMPP started successfully
#if [ $? -ne 0 ]; then
#    echo -e "Error!!!\nRestarting again!!!\n"
#    sudo /opt/lampp/lampp status
#    sudo /opt/lampp/lampp restart

    # Check again after restart
#    if [ $? -ne 0 ]; then
#        echo "Error!!! XAMPP failed to start."
#        sudo /opt/lampp/lampp status
#        exit 1
#    fi
#fi

# Start the XAMPP control panel (if it exists)
#if [ -f "./manager-linux-x64.run" ]; then
#    sudo chmod +x ./manager-linux-x64.run
#    sudo ./manager-linux-x64.run
#else
#    echo "XAMPP control panel not found."
#fi

#echo "XAMPP started successfully."


