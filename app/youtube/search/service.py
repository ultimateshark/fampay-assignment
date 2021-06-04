from sqlalchemy.sql.expression import null
from app import db
from typing import List
from .model import Video
from .interface import VideoInterface
from sqlalchemy import or_


class VideoService():
    @staticmethod
    def get_all(q='') -> List[Video]:
        return Video.query.filter(
            or_(
                Video.title.like('%' + q + '%'),
                Video.description.like('%' + q + '%')
            )
        ).all()

    @staticmethod
    def get_by_id(video_id: int) -> Video:
        return Video.query.get(video_id)

    @staticmethod
    def update(Video: Video, Video_change_updates: VideoInterface) -> Video:
        Video.update(Video_change_updates)
        db.session.commit()
        return Video

    @staticmethod
    def delete_by_id(video_id: int) -> List[int]:
        Video = Video.query.filter(Video.video_id == video_id).first()
        if not Video:
            return []
        db.session.delete(Video)
        db.session.commit()
        return [video_id]

    @staticmethod
    def create(new_attrs: VideoInterface) -> Video:
        new_Video = Video(
            video_id = new_attrs['video_id'],
            title=new_attrs['title'],
            description=new_attrs['description'],
            thumbnail=new_attrs['thumbnail'],
            publish_datetime = new_attrs['publish_datetime']
        )

        db.session.add(new_Video)
        db.session.commit()

        return new_Video