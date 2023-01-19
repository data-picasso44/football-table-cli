from src.standings import Table, StandardTable

class Display:
  def standings(self, teams: list, compact=False):
    if compact:
      standings = Table()
    else:
      standings = StandardTable()

    standings.display(teams)