from source.repositories.competitions_team_repository import CompetitionTeamRepository

class CompetitionTeamService:
    """CompetitionTeam Service class representation."""

    @staticmethod
    def create_from_imported_data(team_id:int=None, competition_id:int=None):
        new_competition_team = {
            'competition_id': competition_id,
            'team_id': team_id
        }
        if not CompetitionTeamRepository().get_relation(new_competition_team):
            CompetitionTeamRepository().create(new_competition_team)

    @staticmethod
    def get_teams_id_by_competition_id(competition_id:int):
        relations = CompetitionTeamRepository().get_all_teams_from_competition(
            competition_id=competition_id
        )
        return [relation.team_id for relation in relations]