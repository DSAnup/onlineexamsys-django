from django.db import models
import uuid

# Create your models here.
class Questions(models.Model):  
    question_cat = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    question_name = models.CharField(max_length=250, blank=False, null= False,)
    question_time = models.FloatField(blank=False, null= False,)
    def __str__(self):
        return self.question_name


class Answers(models.Model):
    answer_choice = models.CharField(max_length=250, blank=False, null= False,)
    question_cat = models.ForeignKey(Questions, blank=False, null= False, on_delete=models.CASCADE, verbose_name='Questions Category')
    Curr_choice= (
        ('0', 'False'),
        ('1', 'True'),
    )
    currect_ans = models.CharField(max_length=1, choices=Curr_choice, null=False, blank=False, verbose_name= 'Choice Currect Answer')
    def __str__(self):
        return self.answer_choice