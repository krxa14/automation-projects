# Week 1: Programming (Python & APIs)

## Project: Multi-Source API Aggregator

### Objectives
- Call multiple public APIs
- Merge, clean, and analyze data
- Output CSV reports
- Handle errors and logging

### Skills Learned
- Python basics: functions, loops, variables
- Requests library for API calls
- JSON parsing
- Error handling

### Project Structure
```
week1-api-project/
├── README.md
├── main.py              # Main script to fetch and process API data
├── api_fetcher.py       # Module for API calls
├── data_processor.py    # Module for data cleaning and merging
├── requirements.txt     # Python dependencies
├── data/               # Directory for output CSV files
└── logs/               # Directory for log files
```

### APIs Used
1. **OpenWeather API** - Weather data
2. **News API** - Latest news articles
3. **JSONPlaceholder** - Sample data for testing

### Implementation Steps

#### Day 1: Planning
- [x] Research free public APIs
- [x] Define data schema
- [x] Plan error handling strategy

#### Day 2-3: Build MVP
- [ ] Set up project structure
- [ ] Implement API fetcher module
- [ ] Create data processing functions
- [ ] Add basic error handling
- [ ] Test with sample data

#### Day 4-5: Challenge & Enhancement
- [ ] Add retry logic for failed API calls
- [ ] Implement rate limiting
- [ ] Create comprehensive logging
- [ ] Add data validation
- [ ] Generate summary statistics
- [ ] Export to CSV with timestamps

### Key Features

1. **API Fetching**
   - Multiple endpoints support
   - Configurable timeout
   - Authentication handling

2. **Data Processing**
   - JSON to DataFrame conversion
   - Missing value handling
   - Data type validation
   - Duplicate removal

3. **Error Handling**
   - Try-except blocks
   - Custom error messages
   - Logging failed requests
   - Retry mechanism

4. **Output Generation**
   - CSV export with timestamps
   - Summary report
   - Error log file

### Dependencies
```
requests==2.31.0
pandas==2.0.3
python-dotenv==1.0.0
```

### Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Run the aggregator
python main.py

# View logs
cat logs/api_aggregator.log
```

### Learning Notes

**What I learned:**
- How to make HTTP requests in Python
- Handling API rate limits
- JSON data structure manipulation
- Pandas DataFrame operations
- Logging best practices

**Challenges faced:**
- API rate limiting issues
- Handling inconsistent data formats
- Managing API keys securely

**Solutions implemented:**
- Used exponential backoff for retries
- Created data normalization functions
- Stored API keys in .env file

### Future Enhancements
- [ ] Add support for more APIs
- [ ] Implement async API calls for better performance
- [ ] Create a simple dashboard for data visualization
- [ ] Add scheduling with cron/scheduler
- [ ] Build a simple web interface

### Resources
- [Requests Documentation](https://requests.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Public APIs List](https://github.com/public-apis/public-apis)

---

**Status:** 🚧 In Progress

**Last Updated:** January 2026
