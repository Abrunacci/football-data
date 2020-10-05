from typing import List

from fastapi import APIRouter, HTTPException

from source.schemas.players_schemas import PlayerSchema
from source.services.players_service import PlayerService
from source.services.teams_players_service import TeamPlayerService


router = APIRouter()


@router.get('/players/{player_id}',
            tags=['Players'],
            response_model=PlayerSchema)
async def get_player_by_id(player_id:int):
    """Get player by id.
    This functions calls the get_player_by_id function from the 
    PlayerService and returns the playerschema for the found item."""
    player = PlayerService.get_player_by_id(player_id=player_id)
    return player


@router.get('/total-players/{competition_code}', 
            tags=['Players'])
async def total_players(competition_code:str):
    """Get Players.
    This function returns all the players in the database.
    """
    players = PlayerService.count_players_by_league_code(code=competition_code)
    return players