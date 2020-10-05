from os import environ
from fastapi import HTTPException
from source.third_party.football_data_connector import FootballDataConnector
from source.services.competitions_service import CompetitionService
from source.services.teams_service import TeamService
from source.services.players_service import PlayerService

class ImporterService:
    """Impoerter service class representation"""

    def __init__(self, *args, **kwargs):
        """Class initialization."""
        self.connector = FootballDataConnector()

    def get_from_connector(self, endpoint:str=None):
        """Get from connector."""
        data = self.connector.get(endpoint=endpoint)
        return data

    def import_competitions_by_code(self, code:str=None):
        """Import competitions by code.
        This functions calls the get_from_connector function and
        create a competition by code.
        """
        if CompetitionService.get_competition_by_code(code):
            raise HTTPException(
                    status_code=409, 
                    detail='League already imported'
            )
        base_endpoint = environ.get('EXTERNAL_API_COMPETITIONS_ENDPOINT')
        endpoint = f'{base_endpoint}/{code}'
        data = self.get_from_connector(endpoint=endpoint)
        if data.get('errorCode') == 400:
            raise HTTPException(status_code=404, detail='Not Found')
        competition = CompetitionService.create_from_imported_data(data=data)
        return competition
        
    def import_teams_by_competition(self, competition_code:str=None):
        """Import teams by competition.
        This functions calls the get_from_connector function with the enpoint
        related to the teams from a competition and create them.
        """
        comp_endpoint = environ.get('EXTERNAL_API_COMPETITIONS_ENDPOINT')
        teams_endpoint = environ.get('EXTERNAL_API_TEAMS_ENDPOINT')
        endpoint = f'{comp_endpoint}/{competition_code}/{teams_endpoint}'
        data = self.get_from_connector(endpoint=endpoint)
        teams_data = data.get('teams')
        competition_id = data.get('competition').get('id')
        teams = TeamService().create_teams_from_competition(
            data=teams_data,
            competition=competition_id
        )
        return teams

    def import_players_by_team(self, team_id:int=None):
        """Import players by teams.
        This functions calls the get_from_connector function with the enpoint
        related to the particular teams get the squad and create the players on
        database.
        """
        teams_endpoint = environ.get('EXTERNAL_API_TEAMS_ENDPOINT')
        endpoint = f'{teams_endpoint}/{team_id}'
        data = self.get_from_connector(endpoint=endpoint)
        team_players = list()
        for member in data.get('squad', []):
            if member.get('role') == 'PLAYER':
                team_players.append(member)
        PlayerService.create_players(team_id=team_id, 
                                     team_players=team_players)
        

    def import_data(self, competition_code):
        """Import data
        This function coordinate the process of data import from the connector.
        """
        competition = self.import_competitions_by_code(code=competition_code)
        teams = self.import_teams_by_competition(
            competition_code=competition_code
        )
        for team in teams:
            self.import_players_by_team(team_id=team.get('id'))
