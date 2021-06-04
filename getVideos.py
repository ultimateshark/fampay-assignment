import argparse
import os

from sqlalchemy.sql.sqltypes import DateTime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app.youtube.search.service import VideoService
from app import create_app
from dateutil import parser as DateParser
DEVELOPER_KEY = 'AIzaSyDOOlIPYxK9bvq2Vj_ZvahDTWWmL-EvY5c'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
env = os.getenv("FLASK_ENV") or "dev"

app = create_app(env)


def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(
    q=options.q,
    part='id,snippet',
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []
  with app.app_context():
    for search_result in search_response.get('items', []):
      if search_result['id']['kind'] == 'youtube#video':
        print('%s' % (search_result['snippet']))
        VideoService.create({
          'video_id': search_result['id']['videoId'],
          'title': search_result['snippet']['title'],
          'description': search_result['snippet']['description'],
          'publish_datetime': DateParser.parse(search_result['snippet']['publishedAt']),
          'thumbnail': search_result['snippet']['thumbnails']['default']['url']
        })

  print('Videos:\n', '\n'.join(videos), '\n')
  print('Channels:\n', '\n'.join(channels), '\n')
  print('Playlists:\n', '\n'.join(playlists), '\n')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='Search term', default='Google')
  parser.add_argument('--max-results', help='Max results', default=25)
  args = parser.parse_args()

  try:
    youtube_search(args)
  except HttpError as e:
    print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))