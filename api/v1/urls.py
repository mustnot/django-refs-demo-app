from django.urls import include
from django.urls import path


app_name = "v1"


urlpatterns = [
    path("posts/", include("api.v1.post.urls")),
]
