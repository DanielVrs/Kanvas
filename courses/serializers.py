from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from courses.models import Course
from students_courses.models import StudentCourse


class CourseSerializer(serializers.ModelSerializer):
    students_courses = serializers.NestedSerializer(child_class=StudentCourse)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Course.objects.all(),
                        message="A user with that name already exists.",
                    )
                ]
            },
            "contents": {"read_only": True},
            "students_courses": {"read_only": True, "many": True},
        }
