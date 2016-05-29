from nba_py import _api_scrape, _get_json
from nba_py.constants import *

class DraftCombineDrill:
    _endpoint = 'draftcombinedrillresults'
    def __init__(self,
                season_year,
                 league_id=League.Default
                 ):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonYear': season_year
                                      })


    def results(self):
        return _api_scrape(self.json, 0)

class DraftStationaryShooting:
    _endpoint = 'draftcombinenonstationaryshooting'
    def __init__(self,
                season_year,
                 league_id=League.Default
                 ):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonYear': season_year
                                      })


    def results(self):
        return _api_scrape(self.json, 0)

class DraftAnthro:
    _endpoint = 'draftcombineplayeranthro'
    def __init__(self,
                season_year,
                 league_id=League.Default
                 ):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonYear': season_year
                                      })


    def results(self):
        return _api_scrape(self.json, 0)

class DraftSpotShooting:
    _endpoint = 'draftcombinespotshooting'
    def __init__(self,
                season_year,
                 league_id=League.Default
                 ):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonYear': season_year
                                      })


    def results(self):
        return _api_scrape(self.json, 0)

class DraftCombineStats:
    _endpoint = 'draftcombinestats'
    def __init__(self,
                season_year,
                 league_id=League.Default
                 ):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonYear': season_year
                                      })


    def results(self):
        return _api_scrape(self.json, 0)
