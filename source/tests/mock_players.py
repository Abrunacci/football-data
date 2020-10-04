from datetime import datetime
from pytest import fixture

from source.models.players import PlayerModel
from source.schemas.players_schemas import PlayerSchema




@fixture(scope='function')
def player_model():
    pass