from django.contrib import admin
from app_game.models import *
# Register your models here.
# admin.site.register(UserProfile)
class AuthorAdmin(admin.ModelAdmin):
    list_display =['user','code']
admin.site.register(Code, AuthorAdmin)


class Author1Admin(admin.ModelAdmin):
    list_display =['user','friend']
admin.site.register(Friend, Author1Admin)