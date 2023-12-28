from django.contrib import admin
from .models import Clients
# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
    list_display = ["name", "web"]

admin.site.register(Clients, ClientsAdmin)
