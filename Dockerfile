# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
COPY .env .env
RUN pip3 install -r requirements.txt
COPY . .
# RUN export GOOGLE_prodELOPER_KEY="AIzaSyDOOlIPYxK9bvq2Vj_ZvahDTWWmL-EvY5c"

EXPOSE 5000
CMD ["python","manage.py","init_db"]
CMD ["python","getVideos.py"]
CMD [ "python3", "wsgi.py"] 