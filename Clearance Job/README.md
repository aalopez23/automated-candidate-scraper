# Clearance Jobs Scraper

Automated web scraper for collecting candidate profile data from Clearance Jobs platform.

## Overview

This module scrapes candidate profiles from Clearance Jobs, a specialized job platform for individuals with security clearances. It extracts comprehensive candidate information including contact details, professional qualifications, and preferences.

## Features

- **Dual Search Support**: Supports both Boolean and Intellisearch query types
- **Comprehensive Data Extraction**: Collects 13+ data points per candidate
- **Automatic Pagination**: Handles multiple pages of results automatically
- **CSV Export**: Saves data in structured CSV format
- **Error Handling**: Gracefully handles missing data fields

## Data Fields Extracted

1. URL - Candidate profile URL
2. Name - Full name
3. Phone Number - Contact phone
4. Email - Contact email
5. Title - Current job title
6. Clearance - Security clearance level
7. Years of Experience (YOE)
8. Relocation Preference
9. Salary - Expected salary range
10. Highest Degree - Education level
11. Military Branch - Military service branch
12. Ideal Locations - Preferred work locations
13. Last Profile Update - When profile was last updated

## Usage

### Configuration

Before running, ensure you have configured your credentials in `config.py`:

```python
CJ_USERNAME = 'your_username'
CJ_PASSWORD = 'your_password'
CJ_SEARCH_QUERY = 'your search query'
CJ_SEARCH_TYPE = True  # True = Boolean, False = Intellisearch
```

### Running the Scraper

```python
from Clearance_Job.cjScrape import bot
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import CJ_USERNAME, CJ_PASSWORD, CJ_SEARCH_QUERY, CJ_SEARCH_TYPE

bot(CJ_USERNAME, CJ_PASSWORD, CJ_SEARCH_QUERY)
```

Or run directly:

```bash
python cjScrape.py
```

### Important Notes

1. **Location Input**: The script provides a 20-second window to manually input location filters on the search page
2. **Excel Files**: Close any Excel files before running to avoid permission errors
3. **Browser**: Chrome browser must be installed (configured for macOS)
4. **File Naming**: Output files are named with date and number of applicants: `cjScrape_(Xapps)_MM_DD_YYYY.csv`
5. **Full Screen**: Keep Chrome in full screen for best results

## Technical Details

- Uses Selenium WebDriver for browser automation
- Implements random delays (3-6 seconds) to mimic human behavior
- Handles dynamic page loading and element detection
- Saves progress incrementally to prevent data loss

## Error Handling

The scraper includes try-except blocks for each data field to handle:
- Missing information
- Changed page structure
- Network timeouts
- Element not found errors

## Output

Results are saved to CSV files in the project root directory. Files are automatically named with the current date and number of applicants scraped.

