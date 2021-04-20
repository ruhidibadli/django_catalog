from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display=("id","name","created_data","isPublished")
    list_display_links=("id","name")
    list_editable=("isPublished",)
    search_fields=("name","description")
    list_per_page=10


# Register your models here.

admin.site.register(Movie,MovieAdmin)