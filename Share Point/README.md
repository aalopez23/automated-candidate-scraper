# SharePoint Resume Scraper

Automated scraper for extracting candidate information from resumes stored in SharePoint.

## Overview

This module scrapes resumes from SharePoint, extracts text content, and uses NLP algorithms to identify and extract candidate information including names, emails, and phone numbers.

## Features

- **Multi-Format Support**: Handles Word documents, PDFs, HTML files, and more
- **NLP-Powered Extraction**: Uses spaCy for intelligent name recognition
- **Regex Pattern Matching**: Extracts emails and phone numbers using pattern matching
- **Duplicate Detection**: Identifies and handles duplicate entries
- **Filtering**: Removes internal contacts and invalid data
- **CSV Export**: Structured data export for analysis

## Components

### spScrape.py
Main scraper script that:
- Authenticates with SharePoint
- Navigates through search results
- Extracts file content
- Coordinates data processing

### spApplicantInfo.py
NLP and extraction functions:
- `name_scrape()` - Extracts names using spaCy NLP
- `email_scrape()` - Regex-based email extraction
- `phone_scrape()` - Phone number extraction and validation
- `count_ints()` - Validates phone number format

### Paste.py
Utility for handling clipboard operations:
- Copies content from SharePoint files
- Saves to temporary text file
- Returns extracted text content

### unitTests.py
Unit testing framework for individual extraction functions.

## Usage

### Prerequisites

1. Install spaCy language model:
```bash
python -m spacy download en_core_web_lg
```

2. Configure credentials in `config.py`:
```python
SP_USERNAME = 'your_email@domain.com'
SP_PASSWORD = 'your_password'
SP_SEARCH_QUERY = 'your search query'
```

### Running the Scraper

```python
from Share_Point.spScrape import bot
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SP_USERNAME, SP_PASSWORD, SP_SEARCH_QUERY

bot(SP_USERNAME, SP_PASSWORD, SP_SEARCH_QUERY)
```

Or run directly:

```bash
python spScrape.py
```

## Data Extraction Process

1. **Authentication**: Logs into SharePoint with provided credentials
2. **Search**: Executes search query to find relevant resumes
3. **File Navigation**: Opens each file and extracts content
4. **Text Extraction**: Copies content to clipboard and processes
5. **NLP Processing**: Uses spaCy to identify names
6. **Pattern Matching**: Extracts emails and phone numbers
7. **Filtering**: Removes duplicates and invalid entries
8. **Export**: Saves structured data to CSV

## Output Format

CSV files contain:
- **URL**: SharePoint file URL
- **File Type**: Word, Excel, PDF, HTML, or Other
- **File Name**: Extracted filename
- **Names (from URL)**: Names extracted from filename
- **Names (from Content)**: Names extracted from resume content
- **Email**: Extracted email addresses
- **Phone**: Extracted and validated phone numbers

## Filtering Rules

### Name Filtering
- Excludes internal contacts (Pamela, Cilinda, etc.)
- Removes common non-name words
- Deduplicates results

### Email Filtering
- Excludes internal email addresses
- Removes no-reply addresses
- Validates email format

### Phone Filtering
- Validates phone number length (10-11 digits)
- Formats phone numbers consistently
- Removes invalid entries

## Technical Details

- **NLP Model**: spaCy `en_core_web_lg` for name entity recognition
- **Browser Automation**: Selenium WebDriver
- **Clipboard Handling**: pyautogui for cross-platform clipboard access
- **File Processing**: Handles various file formats through browser rendering

## Error Handling

The scraper includes robust error handling for:
- File access errors
- Network timeouts
- Invalid file formats
- Missing elements
- Authentication failures

## Testing

Run unit tests to verify extraction functions:

```bash
python unitTests.py
```

Tests can be customized by editing `test_doc.txt` with sample resume text.

