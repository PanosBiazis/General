from pip_search import search

def search_pip(query):
    # Search for packages using pip_search
    results = search(query)
    
    if results:
        print(f"Found {len(results)} results for '{query}':")
        for i, package in enumerate(results[:10]):
            print(f"{i + 1}. {package['name']} - {package['summary']}")
    else:
        print(f"No results found for '{query}'")



# Example usage
search_pip("flask")
