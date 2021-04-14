from django.urls import path,include
from .views import home , report_incident ,youtube_downloader ,download_video



urlpatterns = [
    path('',home,name='home'),
    path('report-incident/',report_incident,name="report_incident"),
    path('yt-downloader/',youtube_downloader,name="youtube-downloader"),
    path('download-video/<str:url>/<int:itag>/',download_video,name="download-video"),
]