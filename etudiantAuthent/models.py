from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# ***************************************


# *****************************************





class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_adminis = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=100)
    annEntre = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return self.nom

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='teacher')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom

class Adminis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='adminis')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=100)
    annEmploi = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom

# **********************************question***********
class Question(models.Model):
    question = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(default=timezone.now)

# ***************lesson*******************************

class Lesson(models.Model):
    lesson = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    created_at = models.DateTimeField(default=timezone.now)

# ***************answer*******************************

class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(default=timezone.now)

# ***************comment*******************************

class Comment(models.Model):
    comment = models.TextField()
    lesson = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)

# ***************students*******************************

class Etudiant(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    tel = models.CharField(max_length=250)
    annEntre = models.CharField(max_length=250)

    def __str__(self):
        return self.nom

# ***************professeur*******************************

class Professeur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    tel = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)

    def __str__(self):
        return self.nom
# *******model pour modul*************REVIEW
class Modul(models.Model):
    modul = models.CharField(max_length=250)

    def __str__(self):
        return self.modul

class Classe(models.Model):
    nom_classe = models.CharField(max_length=250)

    def __str__(self):
        return self.nom_classe

class Filiere(models.Model):
    nom_filiere = models.CharField(max_length=250)

    def __str__(self):
        return self.nom_filiere