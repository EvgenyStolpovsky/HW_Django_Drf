from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from main.models import Lesson, Course
from main.validators import UrlValidator

class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор представление модели Lesson
    """
    # валидатор на url
    link_video = serializers.URLField(validators=[UrlValidator])

    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'course', 'owner', 'link_video',]

