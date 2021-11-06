from django.contrib import admin
from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    model = Flight
    list_display = ('id', 'arrival', 'departure', )
    list_display_links = ('id', )
    search_fields = ('id', )
    list_per_page = 25


admin.site.register(Flight, FlightAdmin)
