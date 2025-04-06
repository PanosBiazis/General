import requests

def search_pypi(query, max_results=10):
    # PyPI JSON search API endpoint
    url = f"https://pypi.org/pypi?%3Aaction=search&term={query}&submit=search"
    
    # Send GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        packages = data.get("packages", [])
        
        if not packages:
            print(f"No results found for '{query}'")
            return
        
        print(f"Found {len(packages)} packages for query '{query}':\n")
        
        # Displaying package names
        for idx, pkg in enumerate(packages[:max_results]):
            print(f"{idx + 1}. {pkg['name']} - {pkg['summary']}")
    else:
        print("Failed to retrieve packages from PyPI")

# Example usage
search_pypi("requests", max_results=10)
