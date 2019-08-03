from rest_framework import serializers
from . import models

class QuestionListView(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('question', 'op1','op2','op3','op4')
