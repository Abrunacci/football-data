from source.repositories.teams_repository import TeamRepository
from .competitions_teams_services import CompetitionTeamService


class TeamService:
    """Team Service class representation."""

    @staticmethod
    def get_team_by_id(team_id:int):
        """Get team by id.
        This function calls the get_by_id function from 
        TeamRepository and returns a team instance when the id 
        it's correct. Otherwise, returns 404.
        
        Arguments
            team_id : int
                An integer that represents the team id
        Returns
            team : TeamModel
                An instance of TeamModel
        """
        team = TeamRepository().get_by_id(team_id)
        return team
    
    @staticmethod
    def get_all():
        """Get all.
        This function calls the get_all function from 
        TeamRepository and returns a list of team instances.
        
        Returns
            teams : List[TeamModel]
                A list of TeamModel instances
        """
        teams = TeamRepository().get_all()
        return teams

    def create_teams_from_competition(self, data:str=None, competition:int=None):
        all_teams = list()
        for team_data in data:
            new_team = {
                'id': team_data.get('id'),
                'name': team_data.get('name'),
                'tla': team_data.get('tla'),
                'email': team_data.get('email'),
                'area_name': team_data.get('area').get('name')
            }
            if not TeamRepository().get_by_id(team_data.get('id')):
                TeamRepository().create(data=new_team)
            all_teams.append(team_data)
            CompetitionTeamService.create_from_imported_data(
                    team_id=team_data.get('id'),
                    competition_id=competition
            )
        return all_teams