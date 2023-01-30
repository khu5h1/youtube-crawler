from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer


class VideoListApiView(viewsets.ModelViewSet, PageNumberPagination):
    serializer_class = VideoSerializer

    def get_queryset(self):
        """
        This view should return a list of all the videos on the basis of filter(if provided else all videos)
        """
        filter = (
            self.request.GET.get("filter") if self.request.GET.get("filter") else ""
        )
        return Video.objects.filter(
            Q(title__icontains=filter) | Q(description__icontains=filter)
        ).order_by("-publishing_timestamp")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
