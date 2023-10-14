from typing import Any
from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Film(TimeStampedModel, TitleDescriptionModel, models.Model):
    class Meta:
        ordering = ['-created']

    class Genre(models.TextChoices):
        COMEDY = 'Comedy'
        HORROR = 'Horror'
        THRILLER = 'Triller'
        DRAMA = 'Drama'

    year_of_issue = models.PositiveSmallIntegerField(validators=[MinValueValidator(1900)])
    rating = models.FloatField(
        null=True, 
        blank=True, 
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )
    genre = models.CharField(
        choices=Genre.choices,
        max_length=20,
    )
    cover = models.ImageField(upload_to='covers')


    def __str__(self) -> str:
        return f'Film {self.title}, id {self.id}, published {self.year_of_issue}'
    

    def get_absolute_url(self) -> Any:
        return reverse('movies:detail', kwargs={'pk': self.pk})
    