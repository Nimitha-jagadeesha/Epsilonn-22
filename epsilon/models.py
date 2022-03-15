from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.postgres.fields import ArrayField

BRANCH_CHOICES = (
    ('CSE', 'CSE'),
    ('ISE', 'ISE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('MECH', 'MECH'),
    ('CIVIL', 'CIVIL'),
    ('ARCH', 'ARCH'),
)
YEAR_CHOICES = (
    ('I', 'I'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('V', 'V'),

)

# Create your models here.


class Question(models.Model):
    number = models.IntegerField(default=0)
    question = models.TextField()
    answer = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    image = models.TextField(default='none.jpg')

    def __str__(self):
        return str(self.number)


class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    question_number = models.IntegerField(default=0)
    last_submit = models.DateTimeField(default=timezone.now)
    visible = models.BooleanField(default=True)
    picked = ArrayField(models.IntegerField(), default=list)
    lifelin1 = models.IntegerField(default=0)
    lifeline2 = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} ({self.last_submit})'


class Display(models.Model):
    display = models.BooleanField(default=False)


class Lifeline(models.Model):
    lifeline = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(
        max_length=6, choices=BRANCH_CHOICES, default='CSE')
    year = models.CharField(max_length=6, choices=YEAR_CHOICES, default='I')


def __str__(self):
    return f'{self.user.username} Profile'


def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
