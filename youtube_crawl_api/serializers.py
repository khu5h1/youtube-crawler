from rest_framework import serializers

from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "title",
            "description",
            "publishing_timestamp",
            "thumbnail_urls",
            "added_to_db",
        ]
