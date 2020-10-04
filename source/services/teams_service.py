from source.repositories.teams_repository import TeamRepository

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