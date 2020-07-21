from django.contrib import admin
from .models import Entry

# Register your models here.

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["user", "title",'city','neighborhood', "created_date", "updated_date"]
    list_display_links = ["user", "title"]
    search_fields = ["user", "title", "created_date"]
    list_filter = ["user", "title", "created_date"]
        
    class Meta:
        model = Entry