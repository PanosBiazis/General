import subprocess

def disable_usb_power_management():
    try:
        # Command to disable USB power management
        power_mgmt_script_path = r"C:\Users\panag\Desktop\Tools_and_Social_Media\DisableUSBPowerManagement.ps1"
        result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', power_mgmt_script_path],
                                capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            print("USB power management disabled successfully.")
        else:
            print("Error disabling USB power management:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def set_high_performance_power_plan():
    try:
        subprocess.run(['powercfg', '/S', 'SCHEME_MIN'], shell=True)
        print("Power plan set to high performance.")
    except Exception as e:
        print(f"An error occurred while setting power plan: {e}")

def disable_startup_apps():
    try:
        subprocess.run(['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run',
                        '/v', 'ExampleApp', '/t', 'REG_BINARY', '/d', '030000000000000000000000', '/f'], shell=True)
        print("Disabled unnecessary startup applications.")
    except Exception as e:
        print(f"An error occurred while disabling startup applications: {e}")

def clear_temp_files():
    try:
        subprocess.run(['del', '/q', '/s', '%temp%\*'], shell=True)
        print("Temporary files cleared.")
    except Exception as e:
        print(f"An error occurred while clearing temp files: {e}")

def disable_visual_effects():
    try:
        subprocess.run(['SystemPropertiesPerformance.exe'], shell=True)
        print("Visual effects adjustment opened. Please configure manually to 'Adjust for best performance'.")
    except Exception as e:
        print(f"An error occurred while opening visual effects settings: {e}")

def enable_fast_startup():
    try:
        subprocess.run(['powercfg', '/hibernate', 'on'], shell=True)
        subprocess.run(['reg', 'add', 'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power',
                        '/v', 'HiberbootEnabled', '/t', 'REG_DWORD', '/d', '1', '/f'], shell=True)
        print("Fast startup enabled.")
    except Exception as e:
        print(f"An error occurred while enabling fast startup: {e}")
        

def disable_hibernation():
    try:
        subprocess.run(['powercfg', '/hibernate', 'off'], shell=True)
        print("Hibernation disabled to save disk space.")
    except Exception as e:
        print(f"An error occurred while disabling hibernation: {e}")

def defragment_and_optimize_drives():
    try:
        # Detecting disk type
        result = subprocess.run(['wmic', 'diskdrive', 'get', 'Model,MediaType'], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            output_lines = result.stdout.splitlines()
            for line in output_lines[1:]:  # Skip the header
                if line.strip():
                    columns = line.split()
                    media_type = columns[-1]  # Last column should be MediaType
                    drive_letter = 'C:'  # Assuming C: drive for simplicity

                    if media_type.lower() == 'hdd':
                        print(f"Detected HDD: {columns[0]}. Running defragmentation.")
                        subprocess.run(['defrag', drive_letter, '/O'], shell=True)
                    elif media_type.lower() == 'ssd':
                        print(f"Detected SSD: {columns[0]}. Running TRIM optimization.")
                        subprocess.run(['powershell', '-Command', f'Optimize-Volume -DriveLetter {drive_letter} -ReTrim -Verbose'], shell=True)
            print("Drives optimized successfully.")
        else:
            print("Error detecting disk type:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred while optimizing drives: {e}")

def update_drivers():
    try:
        subprocess.run(['powershell', '-Command', 'Start-Process', 'ms-settings:windowsupdate'], shell=True)
        print("Windows Update opened for driver updates.")
    except Exception as e:
        print(f"An error occurred while opening Windows Update: {e}")

def disable_background_services():
    try:
        services_to_disable = ["Fax", "XblGameSave", "DiagTrack"]
        for service in services_to_disable:
            subprocess.run(['sc', 'config', service, 'start=disabled'], shell=True)
        print("Non-essential background services disabled.")
    except Exception as e:
        print(f"An error occurred while disabling background services: {e}")

if __name__ == "__main__":
    
    while True:
        
        print("\n1. Disable USB power management")
        
        print("2. Set high performance power plan")
        
        print("3. Disable unnecessary startup applications")
        
        print("4. Clear temporary files")
        
        print("5. Disable visual effects")
        
        print("6. Enable fast startup")
        
        print("7. Disable hibernation")
        
        print("8. Defragment and optimize drives")
        
        print("9. Update drivers")
        
        print("10. Disable background services")
        
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
        
            disable_usb_power_management()
        
        elif choice == "2":
        
            set_high_performance_power_plan()
        
        elif choice == "3":
        
            disable_startup_apps()
        
        elif choice == "4":
        
            clear_temp_files()
        
        elif choice == "5":
        
            disable_visual_effects()
        
        elif choice == "6":
        
            enable_fast_startup()
            
        elif choice == "7":
            
            disable_hibernation()
            
        elif choice == "8":
            
            defragment_and_optimize_drives()
            
        elif choice == "9":
            
            update_drivers()
            
        elif choice == "10":
            
            disable_background_services()
        
        elif choice == "11":
        
            break
        
        else:
            
            print("Invalid choice. Please try again.")
    
    # disable_usb_power_management()
    # set_high_performance_power_plan()
    # disable_startup_apps()
    # clear_temp_files()
    # disable_visual_effects()
    # enable_fast_startup()
