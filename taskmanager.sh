#!/bin/bash

list_tasks() {
    echo "Listing all running processes..."
    ps aux
}

live_list_tasks() {
    echo "Listing all running processes..."
    top
}

search_task() {
    read -p "Enter process name to search: " pname
    pgrep -fl "$pname"
}

kill_task() {
    read -p "Enter PID or process name to kill: " target
    kill "$target" 2>/dev/null || killall "$target" 2>/dev/null
    echo "Attempted to kill $target."
}

force_kill() {
    read -p "Enter PID or process name to force kill: " target
    kill -9 "$target" 2>/dev/null || killall -9 "$target" 2>/dev/null
    echo "Forcefully killed $target."
}

while true; do
    echo "Choose an option:"
    echo "1) List processes"
    echo "2) Live list processes"
    echo "3) Search for a process"
    echo "4) Kill a process"
    echo "5) Force kill a process"
    echo "6) Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1) list_tasks ;;
        2) live_list_tasks ;;
        3) search_task ;;
        4) kill_task ;;
        5) force_kill ;;
        6) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid option, try again." ;;
    esac
done

# chmod +x taskmanager.sh
# ./taskmanager.sh