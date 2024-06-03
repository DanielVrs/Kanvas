from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("courses/", views.ListCreateCourseView.as_view()),
    path("courses/<str:course_id>/", views.RetrieveUpdateDestroyCourseView.as_view()),
]
