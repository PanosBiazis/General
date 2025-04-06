from pip_search import search
import subprocess

def search_and_install_package(query):
    # Search for the package using pip_search
    results = search(query)
    
    if results:
        print(f"Found {len(results)} results for '{query}':")
        for idx, package in enumerate(results[:10]):  # Display first 10 results
            print(f"{idx + 1}. {package['name']} - {package['summary']}")
        
        # Ask user to choose a package by index
        try:
            choice = int(input(f"\nEnter the number of the package you want to install (1-{min(len(results), 10)}): "))
            
            if 1 <= choice <= len(results):
                selected_package = results[choice - 1]['name']
                print(f"Installing {selected_package}...")
                
                # Install the selected package using pip
                subprocess.check_call([subprocess.sys.executable, "-m", "pip", "install", selected_package])
                print(f"{selected_package} has been successfully installed!")
            else:
                print("Invalid choice. Exiting.")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"No results found for '{query}'")

# Ask user for package query
package_query = input("Enter the package you want to search for: ")
search_and_install_package(package_query)
