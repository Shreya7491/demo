from django.db import models

class Question(models.Model):
    question = models.TextField(max_length=255)
    op1 = models.TextField(max_length=255)
    op2 = models.TextField(max_length=255)
    op3 = models.TextField(max_length=255)
    op4 = models.TextField(max_length=255)


    def __str__(self):
        return self.question
