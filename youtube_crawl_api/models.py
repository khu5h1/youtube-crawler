from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    publishing_timestamp = models.DateTimeField()
    thumbnail_urls = models.TextField()
    channel_title = models.CharField(max_length=150)

    # Here unique constraint is added so that no duplicate videos are added to the database
    yt_video_id = models.CharField(max_length=150, unique=True)

    # added_to_db stores the time when the video was added to the database just like created_at and updated_at
    added_to_db = models.DateTimeField(auto_now=True)
    # as there would be no update operations for now, I won't add updated_at field

    def __str__(self):
        return self.title
