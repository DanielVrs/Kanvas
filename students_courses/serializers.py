from rest_framework import serializers
from courses.models import Course

from students_courses.models import StudentCourse


class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = [
            "id",
            "status",
            "course_id",
            "student_id",
            "student_email",
            "student_username",
        ]
        extra_kwargs = {
            "student_email": {"read_only": True},
            "student_username": {"read_only": True},
            "course_id": {"write_only": True},
        }
