"""API Fetcher module for making requests to multiple public APIs."""

import requests
import logging
import time
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class APIFetcher:
    """Handles API calls to multiple public endpoints."""
    
    def __init__(self, timeout: int = 10, max_retries: int = 3):
        """
        Initialize API Fetcher.
        
        Args:
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
        """
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
    
    def _make_request(self, url: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """
        Make HTTP GET request with retry logic.
        
        Args:
            url: API endpoint URL
            params: Query parameters
            
        Returns:
            JSON response as dictionary or None on failure
        """
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Fetching data from {url} (attempt {attempt + 1})")
                response = self.session.get(
                    url,
                    params=params,
                    timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
                
            except requests.exceptions.RequestException as e:
                logger.warning(f"Request failed: {str(e)}")
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.info(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Max retries reached for {url}")
                    return None
    
    def fetch_weather_data(self) -> List[Dict]:
        """
        Fetch weather data from OpenWeather API.
        
        Returns:
            List of weather data dictionaries
        """
        # Using a demo endpoint for testing
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 52.52,
            "longitude": 13.41,
            "current_weather": True
        }
        
        data = self._make_request(url, params)
        if data:
            logger.info("Successfully fetched weather data")
            return [data]
        return []
    
    def fetch_news_data(self) -> List[Dict]:
        """
        Fetch news data from a public API.
        
        Returns:
            List of news article dictionaries
        """
        # Using JSONPlaceholder as example
        url = "https://jsonplaceholder.typicode.com/posts"
        
        data = self._make_request(url)
        if data:
            logger.info(f"Successfully fetched {len(data)} news articles")
            return data[:10]  # Return first 10 for demo
        return []
    
    def fetch_placeholder_data(self) -> List[Dict]:
        """
        Fetch sample data from JSONPlaceholder.
        
        Returns:
            List of user data dictionaries
        """
        url = "https://jsonplaceholder.typicode.com/users"
        
        data = self._make_request(url)
        if data:
            logger.info(f"Successfully fetched {len(data)} user records")
            return data
        return []
    
    def close(self):
        """Close the session."""
        self.session.close()
