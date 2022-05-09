from rest_framework_nested import routers

from django.urls import include
from django.urls import path

from .views import PostViewSet

router = routers.SimpleRouter()
router.register(r"", PostViewSet, basename="posts")


urlpatterns = [
    path("", include(router.urls)),
]
