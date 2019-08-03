from rest_framework import generics

from . import models
from . import serializers

class QuestionListView(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionListView
