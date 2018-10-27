from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Dog(models.Model):

    RESCATADO = 'Rescatado'
    DISPONIBLE = 'Disponible'
    ADOPTADO = 'Adoptado'

    STATE_CHOICES = (
        (RESCATADO, 'Rescatado'),
        (DISPONIBLE, 'Disponible'),
        (ADOPTADO, 'Adoptado'),
    )

    name = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=RESCATADO)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class AdoptionRegister(models.Model):

    owner = models.CharField(max_length=30)
    dogname = models.CharField(max_length=30)

    def publish(self):
        self.save()


    def __str__(self):
        return self.owner