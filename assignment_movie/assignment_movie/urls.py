from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]