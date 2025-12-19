# Setup Guide

This guide will help you set up the Automated Candidate Data Collection System on your local machine.

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser installed
- pip (Python package manager)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Scrap_FALL_INTERN_2022
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install spaCy Language Model

The SharePoint scraper requires the spaCy English language model:

```bash
python -m spacy download en_core_web_lg
```

### 5. Configure Credentials

Create a configuration file from the template:

```bash
cp config.example.py config.py
```

Edit `config.py` and add your credentials:

```python
# Clearance Jobs Credentials
CJ_USERNAME = 'your_username'
CJ_PASSWORD = 'your_password'

# SharePoint Credentials
SP_USERNAME = 'your_email@domain.com'
SP_PASSWORD = 'your_password'

# Search Queries
CJ_SEARCH_QUERY = 'your search query'
SP_SEARCH_QUERY = 'your search query'

# Search Type (True = Boolean, False = Intellisearch)
CJ_SEARCH_TYPE = True
```

**Important**: Never commit `config.py` to version control. It's already in `.gitignore`.

### 6. Verify Installation

Test that all dependencies are installed correctly:

```bash
python -c "import selenium; import spacy; import pandas; print('All dependencies installed successfully!')"
```

## Platform-Specific Notes

### macOS

- Chrome should be installed at `/Applications/Google Chrome.app` (default)
- If Chrome is installed elsewhere, update the `binary_location` in the scraper files

### Windows

- Update the `binary_location` in `cjScrape.py` and `spScrape.py` to point to your Chrome installation
- Example: `options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'`

### Linux

- Install Chrome/Chromium: `sudo apt-get install chromium-browser` (Ubuntu/Debian)
- Update `binary_location` if needed

## Troubleshooting

### ChromeDriver Issues

If you encounter ChromeDriver errors:
- The `webdriver-manager` package should automatically handle ChromeDriver installation
- Ensure Chrome browser is up to date
- Try manually installing ChromeDriver if automatic installation fails

### spaCy Model Not Found

If you get errors about missing spaCy model:
```bash
python -m spacy download en_core_web_lg
```

### Permission Errors

- Ensure Excel files are closed before running scrapers
- Check file permissions in the project directory
- Run with appropriate user permissions

### Import Errors

If you get import errors:
- Ensure you're in the project root directory
- Activate your virtual environment
- Verify all dependencies are installed: `pip list`

## Next Steps

Once setup is complete:

1. Review the main [README.md](README.md) for usage instructions
2. Check module-specific documentation:
   - [Clearance Jobs README](Clearance%20Job/README.md)
   - [SharePoint README](Share%20Point/README.md)
3. Test with a small query first before running large scrapes
4. Review output files in the `excelfiles/` directory

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the code comments in the scraper files
3. Open an issue on GitHub

