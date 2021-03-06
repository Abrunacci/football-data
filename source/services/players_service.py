from source.repositories.players_repository import PlayerRepository
from source.services.competitions_service import CompetitionService
from source.services.competitions_teams_services import CompetitionTeamService
from source.services.teams_players_service import TeamPlayerService

class PlayerService:
    """Player Service class representation."""

    @staticmethod
    def get_player_by_id(player_id:int):
        """Get player by id.
        This function calls the get_by_id function from 
        PlayerRepository and returns a player instance when the id 
        it's correct. Otherwise, returns 404.
        
        Arguments
            player_id : int
                An integer that represents the player id
        Returns
            player : PlayerModel
                An instance of PlayerModel
        """
        player = PlayerRepository().get_by_id(player_id)
        return player
    
    @staticmethod
    def get_all():
        """Get all.
        This function calls the get_all function from 
        PlayerRepository and returns a list of player instances.
        
        Returns
            players : List[PlayerModel]
                A list of PlayerModel instances
        """
        players = PlayerRepository().get_all()
        return players

    @staticmethod
    def create_players(team_id:int=None, team_players:list=None):
        """Create players.
        This function calls the repository function for player creation
        and then calls the TeamPlayerService to create the team relation.
        Arguments:
            team_id : int
                An integer that represents the team id.
            team_players: list
                A list that contains all the player objects for that team.
        """
        for player in team_players:
            new_player = {
                'id': player.get('id'),
                'name': player.get('name'),
                'day_of_birth': player.get('dateOfBirth'),
                'position': player.get('position'),
                'nationality': player.get('nationality'),
                'country_of_birth': player.get('countryOfBirth')

            }
            if not PlayerRepository().get_by_id(new_player.get('id')):
                PlayerRepository().create(new_player)
            TeamPlayerService.create_from_imported_data(
                team_id=team_id,
                player_id=new_player.get('id')
            )

    @staticmethod
    def count_players_by_league_code(code:str):
        """Count players by league code.
        This function obtains the competition from the CompetitionService,
        obtains the teams_id from the CompetitionTeamService and obtains
        the total amount of players from the TeamPlayerService
        
        Arguments:
            code : str
                A string that represents the competition code.
        returns:
            total_players : int
                An integer with the amount of players for that competition
        """
        competition = CompetitionService.get_competition_by_code(code)
        teams_id = CompetitionTeamService.get_teams_id_by_competition_id(
            competition_id=competition.id
        )
        total_players = TeamPlayerService.get_total_players_for_league(teams_id)
        return total_players


            