# Automated Candidate Data Collection System

A Selenium-powered web scraping solution that automates candidate data collection from multiple hiring platforms, eliminating manual data entry and streamlining the hiring pipeline.

## 🎯 Project Overview

This project was developed during a Fall 2022 internship to automate the collection and processing of candidate information from multiple sources. The system significantly reduced manual data entry time and improved hiring efficiency through automated data extraction and categorization.

### Key Achievements

- **Eliminated 15 hours per week** of manual data entry through automation
- **Reduced time-to-hire by 30%** through streamlined candidate evaluation
- Automated data collection from **Clearance Jobs** and **SharePoint** platforms
- Implemented NLP-based algorithms for candidate categorization and evaluation
- **Automated candidate ranking system** scores and ranks candidates based on multiple criteria

## 🚀 Features

### 1. Clearance Jobs Scraper

- Automated profile scraping from Clearance Jobs platform
- Extracts comprehensive candidate information including:
  - Contact details (name, email, phone)
  - Professional information (title, clearance level, years of experience)
  - Preferences (relocation, salary, ideal locations)
  - Education and military background
- Supports both Boolean and Intellisearch query types
- Handles pagination automatically
- Exports data to CSV format

### 2. SharePoint Resume Scraper

- Scrapes resumes stored in SharePoint database
- Extracts text content from various file formats (Word, PDF, HTML)
- Processes multiple file types automatically
- Handles complex SharePoint navigation and authentication

### 3. NLP-Powered Data Extraction

- **Name Extraction**: Uses spaCy NLP to identify candidate names from resumes
- **Email Extraction**: Regex-based email pattern matching
- **Phone Extraction**: Validates and formats phone numbers
- Filters out internal contacts and invalid data
- Categorizes and structures extracted information

### 4. Automated Candidate Ranking & Scoring

- **Intelligent Scoring System**: Automatically scores candidates based on multiple criteria:
  - Years of experience
  - Security clearance level
  - Education level
  - Profile recency (how recently updated)
  - Relocation willingness
  - Salary expectations vs budget
  - Contact information completeness
- **Customizable Weights**: Adjust scoring priorities to match your hiring needs
- **Automatic Ranking**: Candidates are automatically ranked by total score (0-100)
- **Score Breakdown**: See individual scores for each criterion
- **Streamlined Hiring**: Focus on top-ranked candidates first

### 5. Data Processing & Cleaning

- Jupyter notebook for data cleaning and analysis
- Removes duplicates and invalid entries
- Standardizes data format
- Generates clean, analysis-ready datasets

## 📁 Project Structure

```
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── config.example.py        # Configuration template
├── Clearance Job/           # Clearance Jobs scraper module
│   ├── cjScrape.py         # Main scraper script
│   └── README.md           # Module documentation
├── Share Point/            # SharePoint scraper module
│   ├── spScrape.py         # Main scraper script
│   ├── spApplicantInfo.py  # NLP extraction functions
│   ├── Paste.py            # Clipboard handling utility
│   └── unitTests.py        # Unit tests
├── cleaningTable.ipynb     # Data cleaning notebook
├── candidateRanker.py     # Candidate scoring and ranking module
├── ranking_config.example.py  # Ranking configuration template
└── excelfiles/            # Output directory (gitignored)
```

## 🛠️ Technology Stack

- **Python 3.x**
- **Selenium WebDriver** - Web automation and scraping
- **spaCy** - Natural Language Processing for name extraction
- **pandas** - Data manipulation and analysis
- **xlwt** - Excel file generation
- **regex** - Pattern matching for emails and phone numbers
- **phonenumbers** - Phone number validation
- **Custom Ranking Algorithm** - Automated candidate scoring and ranking

## 📦 Installation

See [SETUP.md](SETUP.md) for detailed installation instructions.

Quick start:

1. Clone the repository:

```bash
git clone <repository-url>
cd Scrap_FALL_INTERN_2022
```

2. Install dependencies:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```

3. Configure credentials:

```bash
cp config.example.py config.py
# Edit config.py with your credentials
```

## 🔧 Configuration

Create a `config.py` file (use `config.example.py` as a template) with your credentials:

```python
# Clearance Jobs Credentials
CJ_USERNAME = 'your_username'
CJ_PASSWORD = 'your_password'

# SharePoint Credentials
SP_USERNAME = 'your_email@domain.com'
SP_PASSWORD = 'your_password'

# Search Query
SEARCH_QUERY = 'your search query here'
```

## 💻 Usage

### Candidate Ranking

The ranking system runs automatically after scraping. To customize ranking:

1. Copy the ranking configuration template:

```bash
cp ranking_config.example.py ranking_config.py
```

2. Edit `ranking_config.py` to adjust:

   - Scoring weights (prioritize what matters most)
   - Clearance level scores
   - Education level scores
   - Salary budget (if applicable)

3. The scrapers will automatically use your custom configuration when ranking candidates.

**Example:** To prioritize experience over clearance:

```python
RANKING_WEIGHTS = {
    'years_experience': 0.40,  # Increased from 0.25
    'clearance_level': 0.15,   # Decreased from 0.20
    # ... other weights
}
```

### Clearance Jobs Scraper

```python
from Clearance_Job.cjScrape import bot

# Configure in cjScrape.py or use config.py
bot(username, password, query)
```

The scraper will:

1. Log into Clearance Jobs
2. Execute the search query
3. Navigate through all result pages
4. Extract candidate information
5. Save results to CSV file

### SharePoint Scraper

```python
from Share_Point.spScrape import bot

# Configure in spScrape.py or use config.py
bot(username, password, query)
```

The scraper will:

1. Authenticate with SharePoint
2. Search for resumes matching the query
3. Extract text content from files
4. Process with NLP algorithms
5. Export structured data to CSV

### Data Cleaning

Open `cleaningTable.ipynb` in Jupyter Notebook to:

- Load scraped data
- Clean and standardize entries
- Remove duplicates
- Generate analysis-ready datasets

## 📊 Output Format

Both scrapers generate CSV files with the following structure:

**Clearance Jobs Output:**

- URL, Name, Phone Number, Email, Title, Clearance, Years of Experience, Relocation, Salary, Highest Degree, Military Branch, Ideal Locations, Last Profile Update

**SharePoint Output:**

- URL, File Type, File Name, Names (from URL), Names (from content), Email, Phone

## ⚠️ Important Notes

- **Credentials**: Never commit `config.py` or hardcoded credentials to version control
- **Rate Limiting**: The scrapers include delays to respect website terms of service
- **Browser**: Chrome browser is required (configured for macOS in current setup)
- **Excel Files**: Close any Excel files before running scrapers to avoid permission errors
- **Legal Compliance**: Ensure you have permission to scrape data and comply with website terms of service

## 📈 Candidate Ranking System

The system includes an automated candidate ranking feature that scores and ranks candidates based on multiple criteria. See [RANKING.md](RANKING.md) for detailed documentation.

**Key Features:**

- Automatic scoring on 7 criteria (experience, clearance, education, etc.)
- Customizable weights to match your hiring priorities
- Ranked CSV output with detailed score breakdowns
- Focus on top candidates first to streamline hiring

## 🤝 Contributing

This was an internship project. For improvements or questions, please open an issue.

## 🙏 Acknowledgments

Developed during Fall 2022 internship to support hiring operations and streamline candidate evaluation processes.
