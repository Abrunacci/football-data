from source.repositories.competitions_team_repository import CompetitionTeamRepository

class CompetitionTeamService:
    """CompetitionTeam Service class representation."""
 
    @staticmethod
    def create_from_imported_data(team_id:int=None, competition_id:int=None):
        """Create from imported data.
        This functions creates a competition-team relation on the database.
        
        Arguments:
            team_id : int
                An integer that represent the team_id
            competition_id : int
                An integer that represent the competition_id
        """
        new_competition_team = {
            'competition_id': competition_id,
            'team_id': team_id
        }
        if not CompetitionTeamRepository().get_relation(new_competition_team):
            CompetitionTeamRepository().create(new_competition_team)

    @staticmethod
    def get_teams_id_by_competition_id(competition_id:int):
        """Get teams id by competition_id.
        This function returns all the teams id for a competition
        
        Arguments:
            competition_id : int
                An integer that represent the competition id
        
        Returns:
            teams_list : list
                A list that contains all the teams id related to the 
                competition_id
        """
        data = CompetitionTeamRepository().get_all_teams_from_competition(
            competition_id=competition_id
        )
        teams_list = [relation.team_id for relation in data] 
        return teams_list