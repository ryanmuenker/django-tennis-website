from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'ranking', 'nationality', 'age', 'height')  # Fields to display in the admin list view
    search_fields = ('name', 'nationality')  # Add a search bar for these fields
