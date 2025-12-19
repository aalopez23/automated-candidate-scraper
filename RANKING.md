# Candidate Ranking System

The automated candidate ranking system scores and ranks candidates to help streamline the hiring process by identifying top candidates automatically.

## Overview

After scraping candidate data, the system automatically:
1. Scores each candidate on multiple criteria
2. Calculates a weighted total score (0-100)
3. Ranks candidates from highest to lowest score
4. Generates a ranked CSV file with detailed score breakdowns

## Scoring Criteria

### 1. Years of Experience (25% weight by default)
- Scores increase with more years of experience
- Capped at maximum years (default: 30 years)
- Formula: `(years / max_years) * 100`

### 2. Security Clearance Level (20% weight by default)
- Higher clearance levels score higher
- TS/SCI variants: 95-100 points
- TS: 80 points
- Secret: 60 points
- Public Trust: 30 points
- None: 0 points

### 3. Education Level (15% weight by default)
- PhD/Doctorate: 100 points
- Master's/MBA: 75-80 points
- Bachelor's: 60 points
- Associate's: 40 points
- High School/GED: 15-20 points

### 4. Profile Recency (10% weight by default)
- Recently updated profiles score higher
- Profiles updated within 90 days: 70-100 points
- Older profiles score progressively lower

### 5. Relocation Willingness (10% weight by default)
- Willing to relocate: 100 points
- Not willing: 0 points
- Unknown: 50 points (neutral)

### 6. Salary Match (10% weight by default)
- Only scored if salary budget is configured
- Within budget: 100 points
- Within 10% over budget: 80 points
- Within 20% over budget: 60 points
- Further over budget: Decreasing score

### 7. Contact Information Completeness (10% weight by default)
- Name, email, and phone each contribute 33.33 points
- Complete contact info: 100 points
- Missing information reduces score proportionally

## Customizing Ranking

### Step 1: Create Configuration File

```bash
cp ranking_config.example.py ranking_config.py
```

### Step 2: Adjust Scoring Weights

Edit `ranking_config.py` to prioritize what matters most for your hiring needs:

```python
RANKING_WEIGHTS = {
    'years_experience': 0.30,      # Increased priority
    'clearance_level': 0.25,        # Increased priority
    'education': 0.15,
    'profile_recency': 0.10,
    'relocation': 0.10,
    'salary_match': 0.05,           # Decreased priority
    'contact_completeness': 0.05    # Decreased priority
}
```

**Important:** Weights must sum to 1.0

### Step 3: Adjust Clearance Level Scores

If certain clearance levels are more valuable:

```python
CLEARANCE_LEVELS = {
    'TS/SCI CI Poly': 100,
    'TS/SCI': 95,                  # Slightly lower
    'TS': 85,                      # Increased
    'Secret': 70,                  # Increased
    # ... etc
}
```

### Step 4: Set Salary Budget (Optional)

To enable salary matching:

```python
SALARY_BUDGET = 150000  # Maximum budget in dollars
```

### Step 5: Use Custom Configuration

Modify `candidateRanker.py` to load your config:

```python
from ranking_config import RANKING_WEIGHTS, CLEARANCE_LEVELS, etc.

config = {
    'weights': RANKING_WEIGHTS,
    'clearance_levels': CLEARANCE_LEVELS,
    'education_levels': EDUCATION_LEVELS,
    'max_years_experience': MAX_YEARS_EXPERIENCE,
    'profile_recency_days': PROFILE_RECENCY_DAYS,
    'salary_budget': SALARY_BUDGET
}

ranked_file = rank_clearance_jobs_csv('input.csv', config=config)
```

## Output Format

Ranked CSV files include:

1. **Rank**: Position (1 = highest score)
2. **Total Score**: Weighted score from 0-100
3. **Score Breakdown Columns**:
   - `years_experience Score`
   - `clearance_level Score`
   - `education Score`
   - `profile_recency Score`
   - `relocation Score`
   - `salary_match Score`
   - `contact_completeness Score`
4. **Original Data Columns**: All original candidate data

## Example Use Cases

### Prioritize Experience
```python
RANKING_WEIGHTS = {
    'years_experience': 0.50,  # High priority
    'clearance_level': 0.20,
    'education': 0.15,
    'profile_recency': 0.10,
    'relocation': 0.03,
    'salary_match': 0.01,
    'contact_completeness': 0.01
}
```

### Prioritize Clearance Level
```python
RANKING_WEIGHTS = {
    'clearance_level': 0.40,   # High priority
    'years_experience': 0.25,
    'education': 0.15,
    'profile_recency': 0.10,
    'relocation': 0.05,
    'salary_match': 0.03,
    'contact_completeness': 0.02
}
```

### Budget-Conscious Hiring
```python
SALARY_BUDGET = 120000
RANKING_WEIGHTS = {
    'salary_match': 0.30,      # High priority
    'years_experience': 0.25,
    'clearance_level': 0.20,
    'education': 0.10,
    'profile_recency': 0.08,
    'relocation': 0.05,
    'contact_completeness': 0.02
}
```

## Manual Ranking

You can also rank existing CSV files manually:

```python
from candidateRanker import rank_clearance_jobs_csv, rank_sharepoint_csv

# Rank Clearance Jobs CSV
ranked_file = rank_clearance_jobs_csv('cjScrape_(50apps)_11_15_2022.csv')

# Rank SharePoint CSV
ranked_file = rank_sharepoint_csv('spScrape_(25apps)_11_15_2022.csv')
```

## Understanding Scores

- **90-100**: Excellent match, prioritize these candidates
- **75-89**: Strong match, good candidates
- **60-74**: Moderate match, worth reviewing
- **Below 60**: May not meet key requirements

Remember: Scores are relative to your configured weights and criteria. Adjust weights to match your specific hiring priorities.

## Troubleshooting

### Ranking Not Running
- Ensure `candidateRanker.py` is in the project root
- Check that pandas is installed: `pip install pandas`
- Verify CSV file format matches expected structure

### Scores Seem Incorrect
- Check that data fields are being extracted correctly
- Verify your configuration weights sum to 1.0
- Review score breakdown columns to see individual criterion scores

### Custom Configuration Not Working
- Ensure `ranking_config.py` is in the project root
- Check that you're importing and using the config correctly
- Verify all required keys are present in your config dictionary

