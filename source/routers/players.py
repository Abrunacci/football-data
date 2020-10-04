from typing import List

from fastapi import APIRouter, HTTPException

from source.schemas.players_schemas import PlayerSchema
from source.services.players_service import PlayerService


router = APIRouter()


@router.get('/players/{player_id}',
            tags=['Players'],
            response_model=PlayerSchema)
async def get_player_by_id(player_id:int):
    """Get player by id.
    This functions calls the get_player_by_id function from the 
    PlayerService and returns the playerschema for the found item."""
    print(PlayerService)
    player = PlayerService.get_player_by_id(player_id=player_id)
    print(player)
    return player


@router.get('/players/', 
            tags=['Players'],
            response_model=List[PlayerSchema])
async def get_players():
    """Get Players.
    This function returns all the players in the database.
    """
    players = PlayerService.get_all()
    return players