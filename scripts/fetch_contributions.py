import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_contributions(username, output_path):
    print(f"Fetching contributions for {username}...")
    import time
    url = f"https://github.com/users/{username}/contributions?v={int(time.time())}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # In the modern github contributions graph, each day is a <td class="ContributionCalendar-day" data-date="YYYY-MM-DD" data-level="X">
    days = soup.find_all('td', class_='ContributionCalendar-day')
    
    contributions = []
    
    for day in days:
        date = day.get('data-date')
        if not date:
            continue
        level = day.get('data-level', '0')
        
        contributions.append({
            'date': date,
            'level': int(level)
        })
        
    # Sort by date since HTML has them row-by-row (all Sundays, then all Mondays, etc)
    contributions.sort(key=lambda x: x['date'])
        
    # Check if we got anything
    if not contributions:
        print("Warning: No contributions found. GitHub HTML structure might have changed.")
    else:
        print(f"Found {len(contributions)} days of data.")
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(contributions, f, indent=2)
    print(f"Saved contributions to {output_path}")

if __name__ == "__main__":
    fetch_contributions("Chronos778", "data/contributions.json")
