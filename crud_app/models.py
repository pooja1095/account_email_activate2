from django.db import models

# Create your models here
class Project(models.Model):

    pro_lang = [("c++", "c++"),("python", "python"), ("JAVA", "JAVA"), ("PHP", "PHP"), ("REACTJS", "REACTJS")]

    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_lead = models.CharField(max_length=20)
    programming_language = models.CharField(max_length=100, choices=pro_lang)
    project_start_date = models.DateField()
    project_delivery_date = models.DateField()
