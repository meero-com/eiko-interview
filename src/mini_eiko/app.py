import logging

from marshmallow import ValidationError
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from mini_eiko.endpoints.blurendpoint import BlurEndpoint
from mini_eiko.settings import MEDIA_PATH

logger = logging.getLogger(__name__)


async def startup():
    print('start')
    logger.info('Run startup')


routes = [
    Route('/api/blur', BlurEndpoint),
    Mount('/static', app=StaticFiles(directory=MEDIA_PATH), name='static'),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])
