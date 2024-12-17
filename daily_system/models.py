from django.db import models


class Lesson(models.Model):
    STATUS_CHOICES = [
        ('missing', 'Missing'),
        ('present', 'Present'),
    ]
    date = models.DateTimeField()
    theme = models.CharField(max_length=80)
<<<<<<< HEAD
    presence = models.CharField(max_length=27, 
                    choices=STATUS_CHOICES, default='missing')#відсутність чи присутністьь учня на уроці
    STATUS_CHOICES = [
=======
    presence = models.CharField(max_length=20, choices=[
        ('present', "Present"),
        ('missing', "Missing"),
    ]) #відсутність чи присутністьь учня на уроці

    def __str__(self):
        return f'{self.theme} - {self.date}'
    
    
class Homework(models.Model):
    grade = models.IntegerField()
    homework = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
>>>>>>> 301c715cf2637abb8031b0c35d9cbceaf68cceae
        ('done', "Done"),
        ('in_progress', "In progress"),
        ('to_do', "To do"),
    ]
    grade = models.IntegerField()
    homework = models.CharField(max_length=180)
    status = models.CharField(max_length=27, 
                    choices=STATUS_CHOICES, default='to_do')#виконання домашки
    file = models.FileField(upload_to="comments_media/", blank=True, null=True) #файл виконаного проекта

    

