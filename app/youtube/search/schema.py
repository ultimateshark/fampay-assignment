from marshmallow import fields, Schema


class VideoSchema(Schema):
    videoId = fields.String(attribute="video_id")
    title = fields.String(attribute="title")
    publish_datetime = fields.DateTime(attribute="publish_datetime")
    thumbnail = fields.String(attribute="thumbnail")
    description = fields.String(attribute="description")

class VideoResponseSchema(Schema):
    data = fields.Nested(VideoSchema,many=True)
    page = fields.Number(attribute='page')
    per_page = fields.Number(attribute='per_page')
    total = fields.Number(attribute='total')