from django.contrib import admin
from .models import ContactForm
# Register your models here.

class Contactdata(admin.ModelAdmin):
    list_display=('Name','Email' ,'Subject','Message')


admin.site.register(ContactForm,Contactdata)