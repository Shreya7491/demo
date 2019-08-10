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

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Show
        fields = ('studentno','result')

class IdentifySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Identify
        fields = ('sequence','rollno','answer')
