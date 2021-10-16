from fastapi import FastAPI
from fastapi.params import Depends

from app.config import get_settings, Settings

app = FastAPI()

@app.get('/ping')
async def pong(settings: Settings = Depends(get_settings)):
    return {'ping' : 'pong!',
            'environment' : settings.environment,
            'testing' : settings.testing}
