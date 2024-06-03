from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path(
        "courses/<str:course_id>/students/",
        views.RetrieveUpdateStudentView.as_view(),
    ),
]
