from datetime import datetime
from mypy_extensions import TypedDict


class VideoInterface(TypedDict, total=False):
    video_id: int
    title: str
    description: str
    publish_datetime: datetime
    thumbnail: str