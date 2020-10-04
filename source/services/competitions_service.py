from source.repositories.competitions_repository import CompetitionRepository

class CompetitionService:
    """Competition Service class representation."""

    @staticmethod
    def get_competition_by_id(competition_id:int):
        """Get competition by id.
        This function calls the get_by_id function from 
        CompetitionRepository and returns a competition instance when the id 
        it's correct. Otherwise, returns 404.
        
        Arguments
            competition_id : int
                An integer that represents the competition id
        Returns
            competition : CompetitionModel
                An instance of CompetitionModel
        """
        competition = CompetitionRepository().get_by_id(competition_id)
        return competition
    
    @staticmethod
    def get_all():
        """Get all.
        This function calls the get_all function from 
        CompetitionRepository and returns a list of competition instances.
        
        Returns
            competitions : List[CompetitionModel]
                A list of CompetitionModel instances
        """
        competitions = CompetitionRepository().get_all()
        return competitions