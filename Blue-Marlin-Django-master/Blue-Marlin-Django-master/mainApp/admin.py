from django.contrib import admin

from .models import Booking, Contact

# Register your models here.

class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'order_info']
    search_fields = ['name','name']
    class Meta:
        model = Booking

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['email','details','show_info']
    search_fields = ['email','phone']

    class Meta:
        model = Contact

admin.site.register(Booking, BookingModelAdmin)
admin.site.register(Contact, ContactModelAdmin)
admin.site.site_header = 'Blue Marlin Administration'
