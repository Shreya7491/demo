from rest_framework import serializers
from . import models

class QuestionListView(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('id','question','type', 'op1','op2','op3','op4','ans')


class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Start
        fields = ('name','student_no','normal')
