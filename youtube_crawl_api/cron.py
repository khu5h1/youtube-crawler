import json
import traceback
from time import sleep

from youtube_crawl_api.models import Video
from youtube_crawl_api.services import GoogleAPI


def youtube_fetcher_cron():
    for i in range(0, 6):
        try:
            videos = GoogleAPI().search_for_videos()
            db_videos = [
                Video(
                    title=video.get("snippet", {}).get("title", ""),
                    description=video.get("snippet", {}).get("description", ""),
                    channel_title=video.get("snippet", {}).get("channelTitle", ""),
                    publishing_timestamp=video.get("snippet", {}).get("publishedAt"),
                    thumbnail_urls=json.dumps(
                        video.get("snippet", {}).get("thumbnails", {"default": {}}),
                        indent=4,
                    ),
                    yt_video_id=video.get("id", {}).get("videoId"),
                )
                for video in videos
                if video.get("id", {}).get("kind") == "youtube#video"
                and video.get("snippet")
                and video.get("id")
                and video.get("snippet").get("publishedAt")
            ]
            Video.objects.bulk_create(db_videos, ignore_conflicts=True)
            sleep(10)
        except Exception as e:
            print(e)
            traceback.print_exc()
            continue
