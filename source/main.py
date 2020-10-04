from fastapi import FastAPI
from source.routers import competition, players, teams

app = FastAPI()


app.include_router(competition.router)
app.include_router(players.router)
app.include_router(teams.router)

@app.get('/')
def root():
    return {'hello': 'world', "it":"works"}