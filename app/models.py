from django.db import models
class Question(models.Model):
    question = models.TextField(max_length=1000, unique=True)
    id = models.IntegerField(primary_key=True,unique=True)
    type=models.CharField(max_length=20,blank=True)
    op1 = models.TextField(max_length=255,blank=True)
    op2 = models.TextField(max_length=255,blank=True)
    op3 = models.TextField(max_length=255,blank=True)
    op4 = models.TextField(max_length=255,blank=True)
    ans = models.CharField(max_length=255,blank=True)


    def __str__(self):
        return self.question

class Random_No(models.Model):
    random  = models.CharField(primary_key=True,max_length=255)
    def __str__(self):
        return self.random

class Start(models.Model):
    name=models.CharField(max_length=255)
    student_no = models.IntegerField(primary_key=True,unique=True)
    normal = models.OneToOneField('Random_No',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Identify(models.Model):
    sequence = models.ForeignKey('Question',on_delete=models.CASCADE)
    roll_no = models.ForeignKey('Start',on_delete=models.CASCADE)
    answer = models.CharField(max_length=20)

class Random(models.Model):
    random_no  = models.CharField(primary_key=True,max_length=255)
    def __str__(self):
        return self.random_no

class Show(models.Model):
    studentno = models.ForeignKey('Start',on_delete=models.CASCADE)
    result = models.IntegerField(blank=False)
    random_string = models.OneToOneField('Random',on_delete=models.CASCADE,default='dealdone')
