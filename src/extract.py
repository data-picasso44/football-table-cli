import requests
import json
from dotenv import load_dotenv
import os

class Extractor:
  def __init__(self) -> None:
    self.team_names = []
    self.teams = {}

  def _load_auth_x_token(self) -> str:
    load_dotenv()
    x_auth_token = os.getenv('X_AUTH_TOKEN')
    if x_auth_token is None:
      raise ValueError("X_AUTH_TOKEN variable not found. Please create an account with football-data.org and copy your personal X-Auth token into the .env file.")
    return x_auth_token

  def _request_webpage(self, endpoint: str) -> dict:
    url = "https://api.football-data.org/v4/"
    x_auth_token = self._load_auth_x_token()
    headers = {'X-Auth-Token': x_auth_token}

    response = requests.get(url+endpoint, headers=headers)
    return json.loads(response.text)

  def _write_json(self, data, filename):
    with open('data/' + filename, 'w') as f:
      json.dump(data, f, indent=2)

  def _read_json(self, filename):
    with open('data/' + filename) as f:
      data = json.load(f)
      return data

  def _extract_standings_from_json(self, json_data: dict) -> dict:
    try:
      standings = json_data['standings']
      for  standing in standings:
        if standing['type'] == 'TOTAL':
          standings = standing['table']
          break
      return standings
    except KeyError:
      return None

  def extract_standings(self, id: str, refresh_data=True):
    if refresh_data:
      json_data = self._request_webpage(f'competitions/{id}/standings')
      standings = self._extract_standings_from_json(json_data)
      if standings is None:
        return 'Something wrong with the code. Please check!'
      else:
        json_data = self._read_json('standings.json')

      standings.sort(key=lambda x: x['position'])

      return standings
