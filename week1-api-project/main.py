"""Main script for Multi-Source API Aggregator.

This script fetches data from multiple public APIs,
processes and merges the data, and exports to CSV.
"""

import logging
import sys
from datetime import datetime
import pandas as pd

from api_fetcher import APIFetcher
from data_processor import DataProcessor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/api_aggregator.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Main execution function."""
    logger.info("Starting API Aggregator...")
    
    try:
        # Initialize components
        api_fetcher = APIFetcher()
        data_processor = DataProcessor()
        
        # Fetch data from multiple APIs
        logger.info("Fetching data from APIs...")
        weather_data = api_fetcher.fetch_weather_data()
        news_data = api_fetcher.fetch_news_data()
        placeholder_data = api_fetcher.fetch_placeholder_data()
        
        # Process and merge data
        logger.info("Processing and merging data...")
        merged_data = data_processor.merge_data(
            weather_data,
            news_data,
            placeholder_data
        )
        
        # Clean data
        logger.info("Cleaning data...")
        cleaned_data = data_processor.clean_data(merged_data)
        
        # Export to CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"data/aggregated_data_{timestamp}.csv"
        cleaned_data.to_csv(output_file, index=False)
        logger.info(f"Data exported to {output_file}")
        
        # Generate summary statistics
        logger.info("Generating summary statistics...")
        summary = data_processor.generate_summary(cleaned_data)
        print("\n=== Summary Statistics ===")
        print(summary)
        
        logger.info("API Aggregator completed successfully!")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
