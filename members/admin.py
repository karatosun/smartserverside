from django.contrib import admin
from .models import Collaborator, Researcher


# Register your models here.

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ["id","name", "surname", "rank", "created_date", "updated_date"]
    list_display_links = ["name", "surname"]
    search_fields = ["name", "surname", "rank"]
    list_filter = ['rank', "name", "surname"]
        
    class Meta:
        model = Collaborator

@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ["id","name", "surname", "rank", "created_date", "updated_date"]
    list_display_links = ["name", "surname"]
    search_fields = ["name", "surname", "rank"]
    list_filter = ['rank', "name", "surname"]
        
    class Meta:
        model = Researcher

        