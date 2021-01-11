from django.contrib import admin
from classmates_cards.models import CardModel, ClassmateData


@admin.register(CardModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['number', 'email']


@admin.register(ClassmateData)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country']
