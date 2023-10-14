from django.contrib import admin

from movies.models import Film

@admin.register(Film)
class AdminFilm(admin.ModelAdmin):
    pass
