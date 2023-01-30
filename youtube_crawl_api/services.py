import os
from datetime import datetime, timedelta

import googleapiclient.discovery
from django.conf import settings

from .models import Video


class GoogleAPI:
    def __init__(self):
        self.start_date = datetime.now() - timedelta(hours=24)
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = settings.GOOGLE_API_KEY
        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY
        )

    def search_for_videos(self):
        try:
            from_date_time = (
                Video.objects.latest("publishing_timestamp")
                .publishing_timestamp.astimezone()
                .isoformat()
            )
        except Video.DoesNotExist:
            from_date_time = self.start_date.astimezone().isoformat()
        request = self.youtube.search().list(
            part="snippet",
            maxResults=25,
            order="date",
            publishedAfter=from_date_time,
            type="video",
            regionCode="IN",
        )
        try:
            response = request.execute()
            return response.get("items", [])
        except Exception as e:
            print(e)
            return []
