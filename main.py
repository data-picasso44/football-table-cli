import sys
from src.extract import Extractor
from src.display import Display

e = Extractor()
league_name = input('Insert league name: ')

id  = {
  'Premier League': 'PL',
  'La Liga': 'PD',
  'Serie A': 'SA',
}

teams = e.extract_standings(id[league_name])

display = Display()

if 'compact' in sys.argv or 'c' in sys.argv:
  display.standings(teams, compact=True)
else:
  display.standings(teams)