#%%
# Listing 3.13
import os
from tavily import TavilyClient
from dotenv import load_dotenv
#%%
load_dotenv()
#%%
tavily_client = TavilyClient(os.getenv("TAVILY_API_KEY"))
#%%
def search_web(query: str) -> str:
    """Search the web for the given query."""
    response = tavily_client.search(query, max_results=2, chunks_per_source=2)
    return response.get("results")
#%%
# Listing 3.14
results = search_web("Kipchoge's marathon world record")

# Format and display the results
print("=" * 80)
print("SEARCH RESULTS: Kipchoge's Marathon World Record")
print("=" * 80)

for i, result in enumerate(results, 1):
    print(f"\n📄 Result {i}:")
    print(f"   Title: {result.get('title', 'N/A')}")
    print(f"   URL: {result.get('url', 'N/A')}")
    print(f"   Score: {result.get('score', 'N/A')}")
    print(f"\n   Content:")
    print(f"   {result.get('content', 'N/A')}")
    print("\n" + "-" * 80)
