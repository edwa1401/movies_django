from django.db import models

class Film(models.Model):
    class Meta:
        ordering = ['-rating']

    class Rating(models.IntegerChoices):
        TERRIBLE = 1
        BAD = 2
        SATISFACTORY = 3
        GOOD = 4
        EXCELLENT = 5

    class Genre(models.TextChoices):
        COMEDY = 'Comedy'
        HORROR = 'Horror'
        THRILLER = 'Triller'
        DRAMA = 'Drama'


    title = models.CharField(max_length=200)
    year_of_issue = models.PositiveSmallIntegerField()
    short_description = models.TextField()
    rating = models.SmallIntegerField(
        choices=Rating.choices
        )
    genre = models.CharField(
        choices=Genre.choices,
        max_length=20
        
    )
    cover = models.ImageField(upload_to='covers')