from django.db import models
gender_choice = [('male', 'male'),
                 ('female', 'female')]


class UseModel(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(blank=False, max_length=6, choices=gender_choice)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=20, blank=False)
    confirm_password = models.CharField(max_length=20, blank=False)
