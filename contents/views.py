from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)

from contents.models import Content
from contents.serializers import ContentSerializer
from courses.models import Course


class CreateContentView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        pk = self.kwargs["course_id"]
        course = get_object_or_404(Course, pk=pk)
        serializer.save(course=course)


class RetrieveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    # def get_queryset(self):
    #     course_id = self.kwargs.get("course_id")
    #     content_id = self.kwargs.get("content_id")
    #     course = get_object_or_404(Course, pk=course_id)
    #     content = get_object_or_404(Content, pk=content_id)
    #     return [course, content]
