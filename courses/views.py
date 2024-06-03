from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from courses.models import Course
from courses.serializers import CourseSerializer


class ListCreateCourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"
