"""
Ranking Configuration Example

Copy this file to ranking_config.py and customize the scoring weights and criteria
to match your hiring priorities.
"""

# Scoring weights (must sum to 1.0)
RANKING_WEIGHTS = {
    'years_experience': 0.25,      # Weight for years of experience
    'clearance_level': 0.20,        # Weight for security clearance level
    'education': 0.15,              # Weight for education level
    'profile_recency': 0.10,        # Weight for how recent the profile is
    'relocation': 0.10,             # Weight for relocation willingness
    'salary_match': 0.10,           # Weight for salary expectations match
    'contact_completeness': 0.10    # Weight for complete contact information
}

# Security clearance level scores (0-100)
CLEARANCE_LEVELS = {
    'TS/SCI': 100,
    'TS/SCI CI Poly': 100,
    'TS/SCI Full Scope': 100,
    'TS/SCI Poly': 95,
    'TS/SCI CI': 95,
    'TS': 80,
    'Secret': 60,
    'Interim Secret': 50,
    'Public Trust': 30,
    'None': 0
}

# Education level scores (0-100)
EDUCATION_LEVELS = {
    'PhD': 100,
    'Doctorate': 100,
    'Ph.D.': 100,
    'Master': 80,
    'Masters': 80,
    'MBA': 75,
    'Bachelor': 60,
    'Bachelors': 60,
    'BA': 60,
    'BS': 60,
    'Associate': 40,
    'High School': 20,
    'GED': 15
}

# Maximum years of experience for scoring (capped at this value)
MAX_YEARS_EXPERIENCE = 30

# Profile recency threshold (days)
# Profiles updated within this many days are considered "recent"
PROFILE_RECENCY_DAYS = 90

# Salary budget (optional)
# Set to None to disable salary matching, or set to maximum budget number
SALARY_BUDGET = None  # Example: 150000

# Example: To use this configuration in candidateRanker.py:
# from ranking_config import RANKING_WEIGHTS, CLEARANCE_LEVELS, etc.
# config = {
#     'weights': RANKING_WEIGHTS,
#     'clearance_levels': CLEARANCE_LEVELS,
#     'education_levels': EDUCATION_LEVELS,
#     'max_years_experience': MAX_YEARS_EXPERIENCE,
#     'profile_recency_days': PROFILE_RECENCY_DAYS,
#     'salary_budget': SALARY_BUDGET
# }
# ranker = CandidateRanker(config)

