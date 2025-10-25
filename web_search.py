"""Web Search Module for Lisa-Agent

Provides real-time web search capabilities using DuckDuckGo API.
Falls back to Bing search if needed.
"""

import requests
from typing import Dict, List, Optional
import json


class WebSearchEngine:
    """Handles web searches using DuckDuckGo and Bing APIs"""
    
    def __init__(self, bing_api_key: Optional[str] = None):
        """
        Initialize the search engine.
        
        Args:
            bing_api_key: Optional Bing API key for enhanced search
        """
        self.bing_api_key = bing_api_key
        self.ddg_base_url = "https://api.duckduckgo.com/"
        self.bing_base_url = "https://api.bing.microsoft.com/v7.0/search"
        
    def search_duckduckgo(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Search using DuckDuckGo Instant Answer API.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of search result dictionaries
        """
        try:
            params = {
                'q': query,
                'format': 'json',
                'no_html': 1,
                'skip_disambig': 1
            }
            
            response = requests.get(self.ddg_base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            results = []
            
            # Extract abstract if available
            if data.get('Abstract'):
                results.append({
                    'title': data.get('Heading', 'Result'),
                    'snippet': data['Abstract'],
                    'url': data.get('AbstractURL', ''),
                    'source': 'DuckDuckGo'
                })
            
            # Extract related topics
            for topic in data.get('RelatedTopics', [])[:max_results - len(results)]:
                if isinstance(topic, dict) and 'Text' in topic:
                    results.append({
                        'title': topic.get('Text', '').split(' - ')[0] if ' - ' in topic.get('Text', '') else 'Related',
                        'snippet': topic.get('Text', ''),
                        'url': topic.get('FirstURL', ''),
                        'source': 'DuckDuckGo'
                    })
            
            return results[:max_results]
            
        except Exception as e:
            print(f"DuckDuckGo search error: {e}")
            return []
    
    def search_bing(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Search using Bing Search API (requires API key).
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of search result dictionaries
        """
        if not self.bing_api_key:
            return []
        
        try:
            headers = {'Ocp-Apim-Subscription-Key': self.bing_api_key}
            params = {'q': query, 'count': max_results, 'textDecorations': False}
            
            response = requests.get(self.bing_base_url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get('webPages', {}).get('value', [])[:max_results]:
                results.append({
                    'title': item.get('name', ''),
                    'snippet': item.get('snippet', ''),
                    'url': item.get('url', ''),
                    'source': 'Bing'
                })
            
            return results
            
        except Exception as e:
            print(f"Bing search error: {e}")
            return []
    
    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Perform web search using available engines.
        Tries DuckDuckGo first, falls back to Bing if available.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of search result dictionaries
        """
        # Try DuckDuckGo first (free, no API key needed)
        results = self.search_duckduckgo(query, max_results)
        
        # If no results and Bing API is available, try Bing
        if not results and self.bing_api_key:
            results = self.search_bing(query, max_results)
        
        return results
    
    def format_results(self, results: List[Dict]) -> str:
        """
        Format search results as readable text.
        
        Args:
            results: List of search result dictionaries
            
        Returns:
            Formatted string representation of results
        """
        if not results:
            return "No results found."
        
        formatted = "Search Results:\n\n"
        for i, result in enumerate(results, 1):
            formatted += f"{i}. {result.get('title', 'No title')}\n"
            formatted += f"   {result.get('snippet', 'No description')}\n"
            if result.get('url'):
                formatted += f"   URL: {result['url']}\n"
            formatted += "\n"
        
        return formatted.strip()


def web_search(query: str, bing_api_key: Optional[str] = None, max_results: int = 5) -> str:
    """
    Convenience function for quick web searches.
    
    Args:
        query: Search query string
        bing_api_key: Optional Bing API key
        max_results: Maximum number of results to return
        
    Returns:
        Formatted search results as string
    """
    engine = WebSearchEngine(bing_api_key=bing_api_key)
    results = engine.search(query, max_results=max_results)
    return engine.format_results(results)


if __name__ == "__main__":
    # Example usage
    print("Testing Web Search Module...\n")
    
    # Test search
    query = "artificial intelligence"
    print(f"Searching for: {query}\n")
    results = web_search(query, max_results=3)
    print(results)
