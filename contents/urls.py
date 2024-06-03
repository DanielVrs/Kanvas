from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("courses/<str:course_id>/contents/", views.CreateContentView.as_view()),
    path(
        "courses/<str:course_id>/contents/<str:content_id>/",
        views.RetrieveUpdateDestroyContentView.as_view(),
    ),
]
