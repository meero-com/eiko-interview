from marshmallow import ValidationError
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

from mini_eiko.processors.blurprocessor import BlurProcessor
from mini_eiko.schemas.blurendpointschema import BlurEndpointSchema


class BlurEndpoint(HTTPEndpoint):
    async def get(self, request: Request):
        return JSONResponse({'hello': 'world'})

    async def post(self, request: Request):

        payload = await request.json()

        schema = BlurEndpointSchema()
        data = schema.load(payload)
        print(data)

        processor = BlurProcessor()
        image_name = await processor.process(data['url'])

        return JSONResponse({'success': True, 'url': request.base_url.components.geturl() + 'static/' + image_name})
