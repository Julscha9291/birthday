import csv
from django.contrib import admin
from rsvp.models import Guest
from rsvp.models import Drink
from django.shortcuts import render
from django.urls import path
from .views import guest_summary
from django.http import HttpResponse


# Exportfunktion
def export_guests_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="guests.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Anwesenheit', 'Gäste', 'RSVP-Datum'])

    for guest in queryset:
        writer.writerow([guest.name, guest.attendance, guest.rsvp_date])

    return response

export_guests_csv.short_description = 'Exportiere ausgewählte Gäste als CSV'

# Restlicher Code
    
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'attendance','get_drinks', 'rsvp_date')
    actions = [export_guests_csv]

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('guest_summary/', self.admin_site.admin_view(self.guest_summary_view), name='guest_summary'),
        ]
        return custom_urls + urls

    def guest_summary_view(self, request):
        attending_guests = Guest.objects.filter(attendance='Ich nehme teil').count()
        not_attending_guests = Guest.objects.filter(attendance='Ich nehme nicht teil').count()

        context = {
            'attending_guests': attending_guests,
            'not_attending_guests': not_attending_guests,
        }

        return render(request, 'admin/guest_summary.html', context)
    
    def get_drinks(self, obj):
        return ", ".join([drinks.name for drinks in obj.drinks.all()])
    get_drinks.short_description = 'Getränke' 

admin.site.register(Guest, GuestAdmin)

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_selection_count')

    def get_selection_count(self, obj):
        return obj.guest_set.count()

    get_selection_count.short_description = 'Auswahlanzahl'

admin.site.register(Drink, DrinkAdmin)


