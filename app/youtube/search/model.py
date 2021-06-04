from sqlalchemy import Integer, Column, String, DateTime, Text
from app import db
from .interface import VideoInterface
from typing import Any


class Video(db.Model):
    __tablename__ = "videos"

    id = Column(Integer(),primary_key=True,autoincrement=True)
    video_id = Column(String())
    title = Column(String(255),index=True)
    description = Column(Text())
    publish_datetime = Column(DateTime())
    thumbnail = Column(String(255))

    def update(self, changes: VideoInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self