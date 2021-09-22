from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254)