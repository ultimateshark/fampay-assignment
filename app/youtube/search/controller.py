from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .schema import VideoSchema,VideoResponseSchema
from .service import VideoService
from .model import Video

api = Namespace("Videos", description="Youtube Search video controller")


@api.route("/")
class VideoResource(Resource):
    @responds(schema=VideoResponseSchema)
    def get(self,) -> List[Video]:
        args = request.args
        q = ''
        page = int(args.get('page')) if args.get('page') else 0
        per_page = int(args.get('per_page')) if args.get('per_page') else 15
        return VideoService.get_all(q,page,per_page)

@api.route("/search")
class VideoResource(Resource):
    @responds(schema=VideoResponseSchema)
    def get(self,) -> List[Video]:
        args = request.args
        q = args.get('q') if args.get('q') else ''
        page = int(args.get('page')) if args.get('page') else 0
        per_page = int(args.get('per_page')) if args.get('per_page') else 15
        return VideoService.get_all(q,page,per_page)