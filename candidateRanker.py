"""
Candidate Ranking and Scoring Module

This module provides automated candidate scoring and ranking based on multiple criteria
to streamline the hiring process and identify top candidates.
"""

import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class CandidateRanker:
    """
    Scores and ranks candidates based on configurable criteria.
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the ranker with scoring configuration.
        
        Args:
            config: Dictionary with scoring weights and criteria. If None, uses defaults.
        """
        self.config = config or self._default_config()
    
    def _default_config(self) -> Dict:
        """Default scoring configuration."""
        return {
            'weights': {
                'years_experience': 0.25,
                'clearance_level': 0.20,
                'education': 0.15,
                'profile_recency': 0.10,
                'relocation': 0.10,
                'salary_match': 0.10,
                'contact_completeness': 0.10
            },
            'clearance_levels': {
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
            },
            'education_levels': {
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
            },
            'max_years_experience': 30,  # Cap for scoring
            'profile_recency_days': 90,  # Consider profiles updated within 90 days as recent
            'salary_budget': None,  # Set to a number to enable salary matching
        }
    
    def score_years_experience(self, yoe: str) -> float:
        """
        Score based on years of experience.
        
        Args:
            yoe: Years of experience string (e.g., "5 years", "10+ years")
        
        Returns:
            Score from 0-100
        """
        if not yoe or yoe.strip() == '':
            return 0
        
        # Extract number from string
        numbers = re.findall(r'\d+', yoe)
        if not numbers:
            return 0
        
        years = int(numbers[0])
        max_years = self.config['max_years_experience']
        
        # Score increases with experience, capped at max_years
        score = min((years / max_years) * 100, 100)
        return round(score, 2)
    
    def score_clearance_level(self, clearance: str) -> float:
        """
        Score based on security clearance level.
        
        Args:
            clearance: Clearance level string
        
        Returns:
            Score from 0-100
        """
        if not clearance or clearance.strip() == '':
            return 0
        
        clearance_upper = clearance.upper()
        levels = self.config['clearance_levels']
        
        # Check for exact match first
        for level, score in levels.items():
            if level.upper() in clearance_upper:
                return float(score)
        
        # Default score if not found
        return 20
    
    def score_education(self, degree: str) -> float:
        """
        Score based on education level.
        
        Args:
            degree: Highest degree string
        
        Returns:
            Score from 0-100
        """
        if not degree or degree.strip() == '':
            return 0
        
        degree_upper = degree.upper()
        education_levels = self.config['education_levels']
        
        # Check for match
        for level, score in education_levels.items():
            if level.upper() in degree_upper:
                return float(score)
        
        # Default score if not found
        return 30
    
    def score_profile_recency(self, last_update: str) -> float:
        """
        Score based on how recently the profile was updated.
        
        Args:
            last_update: Last update date string
        
        Returns:
            Score from 0-100 (100 = very recent, 0 = old)
        """
        if not last_update or last_update.strip() == '':
            return 0
        
        try:
            # Try to parse various date formats
            date_str = last_update.strip()
            
            # Handle relative dates (e.g., "2 days ago", "1 week ago")
            if 'day' in date_str.lower() or 'week' in date_str.lower() or 'month' in date_str.lower():
                numbers = re.findall(r'\d+', date_str)
                if numbers:
                    num = int(numbers[0])
                    if 'day' in date_str.lower():
                        days_ago = num
                    elif 'week' in date_str.lower():
                        days_ago = num * 7
                    elif 'month' in date_str.lower():
                        days_ago = num * 30
                    else:
                        days_ago = 365
                else:
                    days_ago = 365
            else:
                # Try parsing absolute dates
                # Common formats: MM/DD/YYYY, YYYY-MM-DD, etc.
                for fmt in ['%m/%d/%Y', '%Y-%m-%d', '%m-%d-%Y', '%B %d, %Y']:
                    try:
                        update_date = datetime.strptime(date_str, fmt)
                        days_ago = (datetime.now() - update_date).days
                        break
                    except ValueError:
                        continue
                else:
                    return 0
            
            # Score decreases as days_ago increases
            recency_days = self.config['profile_recency_days']
            if days_ago <= recency_days:
                score = 100 - (days_ago / recency_days) * 30  # 100 to 70 for recent profiles
            else:
                score = max(70 - ((days_ago - recency_days) / 30) * 70, 0)  # 70 to 0 for older
            
            return round(max(score, 0), 2)
        except:
            return 0
    
    def score_relocation(self, relocation: str) -> float:
        """
        Score based on relocation willingness.
        
        Args:
            relocation: Relocation preference string
        
        Returns:
            Score from 0-100 (100 = willing, 0 = not willing)
        """
        if not relocation or relocation.strip() == '':
            return 50  # Neutral score if unknown
        
        relo_lower = relocation.lower()
        
        if any(word in relo_lower for word in ['yes', 'willing', 'open', 'consider', 'relocate']):
            return 100
        elif any(word in relo_lower for word in ['no', 'not', 'unwilling', 'refuse']):
            return 0
        else:
            return 50  # Neutral
    
    def score_salary_match(self, salary: str, budget: Optional[float] = None) -> float:
        """
        Score based on salary expectations vs budget.
        
        Args:
            salary: Salary range string
            budget: Maximum budget (optional)
        
        Returns:
            Score from 0-100
        """
        if not salary or salary.strip() == '':
            return 50  # Neutral if unknown
        
        budget = budget or self.config.get('salary_budget')
        if not budget:
            return 50  # Can't score without budget
        
        # Extract numbers from salary string
        numbers = re.findall(r'[\d,]+', salary.replace(',', ''))
        if not numbers:
            return 50
        
        # Get the highest number (assuming it's a range)
        try:
            max_salary = max([int(n.replace(',', '')) for n in numbers])
            
            # Score higher if salary is within or below budget
            if max_salary <= budget:
                return 100
            elif max_salary <= budget * 1.1:  # Within 10% over budget
                return 80
            elif max_salary <= budget * 1.2:  # Within 20% over budget
                return 60
            else:
                return max(100 - ((max_salary - budget) / budget) * 100, 0)
        except:
            return 50
    
    def score_contact_completeness(self, name: str, email: str, phone: str) -> float:
        """
        Score based on completeness of contact information.
        
        Args:
            name: Candidate name
            email: Email address
            phone: Phone number
        
        Returns:
            Score from 0-100
        """
        score = 0
        if name and name.strip():
            score += 33.33
        if email and email.strip():
            score += 33.33
        if phone and phone.strip():
            score += 33.34
        
        return round(score, 2)
    
    def calculate_total_score(self, candidate_data: Dict) -> Tuple[float, Dict]:
        """
        Calculate total weighted score for a candidate.
        
        Args:
            candidate_data: Dictionary with candidate information
        
        Returns:
            Tuple of (total_score, score_breakdown)
        """
        weights = self.config['weights']
        breakdown = {}
        
        # Score each criterion
        breakdown['years_experience'] = self.score_years_experience(
            candidate_data.get('YOE', '') or candidate_data.get('Years of Experience', '')
        )
        
        breakdown['clearance_level'] = self.score_clearance_level(
            candidate_data.get('Clearance', '') or candidate_data.get('Clearance Level', '')
        )
        
        breakdown['education'] = self.score_education(
            candidate_data.get('Highest Degree', '') or candidate_data.get('Degree', '')
        )
        
        breakdown['profile_recency'] = self.score_profile_recency(
            candidate_data.get('Last Profile Update', '') or candidate_data.get('Last Update', '')
        )
        
        breakdown['relocation'] = self.score_relocation(
            candidate_data.get('Relocation?', '') or candidate_data.get('Relocation', '')
        )
        
        breakdown['salary_match'] = self.score_salary_match(
            candidate_data.get('Salary', '') or candidate_data.get('Salary Range', '')
        )
        
        breakdown['contact_completeness'] = self.score_contact_completeness(
            candidate_data.get('Name', ''),
            candidate_data.get('E-Mail', '') or candidate_data.get('Email', ''),
            candidate_data.get('Phone Number', '') or candidate_data.get('Phone', '')
        )
        
        # Calculate weighted total
        total_score = sum(
            breakdown[criterion] * weights.get(criterion, 0)
            for criterion in breakdown.keys()
        )
        
        return round(total_score, 2), breakdown
    
    def rank_candidates(self, candidates: List[Dict]) -> List[Dict]:
        """
        Rank candidates by their total scores.
        
        Args:
            candidates: List of candidate dictionaries
        
        Returns:
            List of candidates sorted by score (highest first), with scores added
        """
        scored_candidates = []
        
        for candidate in candidates:
            total_score, breakdown = self.calculate_total_score(candidate)
            candidate['Total Score'] = total_score
            candidate['Score Breakdown'] = breakdown
            scored_candidates.append(candidate)
        
        # Sort by total score (descending)
        scored_candidates.sort(key=lambda x: x.get('Total Score', 0), reverse=True)
        
        # Add rank
        for rank, candidate in enumerate(scored_candidates, start=1):
            candidate['Rank'] = rank
        
        return scored_candidates


def rank_clearance_jobs_csv(csv_file: str, output_file: Optional[str] = None, 
                            config: Optional[Dict] = None) -> str:
    """
    Rank candidates from a Clearance Jobs CSV file.
    
    Args:
        csv_file: Path to input CSV file
        output_file: Path to output CSV file (if None, adds '_ranked' to input filename)
        config: Optional ranking configuration
    
    Returns:
        Path to output file
    """
    import pandas as pd
    
    ranker = CandidateRanker(config)
    
    # Read CSV
    df = pd.read_csv(csv_file)
    
    # Convert to list of dictionaries
    candidates = df.to_dict('records')
    
    # Rank candidates
    ranked_candidates = ranker.rank_candidates(candidates)
    
    # Convert back to DataFrame
    result_data = []
    for candidate in ranked_candidates:
        row = candidate.copy()
        # Flatten score breakdown
        breakdown = row.pop('Score Breakdown', {})
        for key, value in breakdown.items():
            row[f'{key} Score'] = value
        result_data.append(row)
    
    result_df = pd.DataFrame(result_data)
    
    # Reorder columns to put Rank and Total Score first
    cols = ['Rank', 'Total Score'] + [c for c in result_df.columns if c not in ['Rank', 'Total Score']]
    result_df = result_df[[c for c in cols if c in result_df.columns]]
    
    # Save to CSV
    if output_file is None:
        output_file = csv_file.replace('.csv', '_ranked.csv')
    
    result_df.to_csv(output_file, index=False)
    return output_file


def rank_sharepoint_csv(csv_file: str, output_file: Optional[str] = None,
                       config: Optional[Dict] = None) -> str:
    """
    Rank candidates from a SharePoint CSV file.
    
    Args:
        csv_file: Path to input CSV file
        output_file: Path to output CSV file (if None, adds '_ranked' to input filename)
        config: Optional ranking configuration (adjusted for SharePoint data)
    
    Returns:
        Path to output file
    """
    import pandas as pd
    
    # Adjust config for SharePoint (less data available)
    if config is None:
        config = {}
    
    sp_config = {
        'weights': {
            'contact_completeness': 0.40,
            'profile_recency': 0.30,
            'education': 0.30
        },
        **config
    }
    
    ranker = CandidateRanker(sp_config)
    
    # Read CSV
    df = pd.read_csv(csv_file)
    
    # Convert to list of dictionaries
    candidates = df.to_dict('records')
    
    # Map SharePoint columns to expected format
    for candidate in candidates:
        # Map names
        if 'Content - Names' in candidate:
            candidate['Name'] = candidate.get('Content - Names', '')
        elif 'URL - Names' in candidate:
            candidate['Name'] = candidate.get('URL - Names', '')
        
        # Map email and phone
        if 'Content - Email' in candidate:
            candidate['Email'] = candidate.get('Content - Email', '')
        if 'Content - Phone' in candidate:
            candidate['Phone'] = candidate.get('Content - Phone', '')
    
    # Rank candidates
    ranked_candidates = ranker.rank_candidates(candidates)
    
    # Convert back to DataFrame
    result_data = []
    for candidate in ranked_candidates:
        row = candidate.copy()
        breakdown = row.pop('Score Breakdown', {})
        for key, value in breakdown.items():
            row[f'{key} Score'] = value
        result_data.append(row)
    
    result_df = pd.DataFrame(result_data)
    
    # Reorder columns
    cols = ['Rank', 'Total Score'] + [c for c in result_df.columns if c not in ['Rank', 'Total Score']]
    result_df = result_df[[c for c in cols if c in result_df.columns]]
    
    # Save to CSV
    if output_file is None:
        output_file = csv_file.replace('.csv', '_ranked.csv')
    
    result_df.to_csv(output_file, index=False)
    return output_file


if __name__ == "__main__":
    # Example usage
    print("Candidate Ranker Module")
    print("Use rank_clearance_jobs_csv() or rank_sharepoint_csv() to rank candidates from CSV files")

