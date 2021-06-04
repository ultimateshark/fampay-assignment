from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .schema import VideoSchema
from .service import VideoService
from .model import Video

api = Namespace("Videos", description="Youtube Search video controller")


@api.route("/")
class VideoResource(Resource):
    @responds(schema=VideoSchema, many=True)
    def get(self,) -> List[Video]:
        args = request.args
        q = args.get('q') if args.get('q') else ''
        return VideoService.get_all(q)

    @accepts(schema=VideoSchema, api=api)
    @responds(schema=VideoSchema)
    def post(self) -> Video:
        return VideoService.create(request.parsed_obj)