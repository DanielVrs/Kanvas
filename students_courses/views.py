from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.response import Response
from accounts.models import Account
from courses.models import Course
from courses.serializers import CourseSerializer
from students_courses.models import StudentCourse


class RetrieveUpdateStudentView(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # lookup_url_kwarg = "course_id"

    def perform_update(self, serializer):
        pk = self.kwargs.get("course_id")
        course = get_object_or_404(Course, pk=pk)

        for data in self.request.data:
            email = data["student_email"]
            students = get_object_or_404(Account, email=email)
            data = StudentCourse.objects.create(
                course_id=course["id"],
                student_id=students["id"],
            )

        serializer = self.get_serializer(data=..., partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
