from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .models import Booking, Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def packages(request):
    return render(request, 'packages.html')

def online_booking(request):
    return render(request, 'online_booking.html')

def contact(request):
    return render(request, 'contact.html')

def store_booking(request):
    if request.method == 'POST':
        booking = Booking()
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']

        
        booking.name = name
        booking.email = email
        booking.description = description

        if(name and email and description):
            booking.save()
            messages.info(request, "Thank You, your information is sent to the admin, we'll let you inform soon")
            return render(request, 'online_booking.html')
        #Booking.objects.create(name, email, description)
        return render(request, 'online_booking.html')
    else:
        return render(request, 'online_booking.html')


def store_contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        details = request.POST['details']
        
        contact = Contact()
        contact.email = email
        contact.phone = phone
        contact.details = details

        if(email and phone and details):
            contact.save()
            messages.info(request, "Thank You, your information is sent to the admin, we'll let you inform soon")
            return render(request, 'contact.html')
        else:
            return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')



def venus(request):
    return render(request, 'packages/venus.html')


def photographer(request):
    return render(request, 'packages/photographers.html')

def makeup_artists(request):
    return render(request, 'packages/makeup_artists.html')

def mehendi_artists(request):
    return render(request, 'packages/mehendi_artists.html')

def bridal_wear(request):
    return render(request, 'packages/bridal_wear.html')

def groom_wear(request):
    return render(request, 'packages/groom_wear.html')

def kazi(request):
    return render(request, 'packages/kazi_office.html')


def decorators(request):
    return render(request, 'packages/decorators.html')

def caterers(request):
    return render(request, 'packages/caterers.html')

def dj_and_live(request):
    return render(request, 'packages/dj_and_live.html')

def invite(request):
    return render(request, 'packages/invite.html')

def other_services(request):
    return render(request, 'packages/other_services.html')

def dhaka_services(request):
    return render(request, 'packages/dhaka_services.html')

def chittagong_services(request):
    return render(request, 'packages/chittagong_services.html')

def rajshahi_services(request):
    return render(request, 'packages/rajshahi_services.html')

def black_car(request):
    return render(request, 'packages/black_car.html')

def white_car(request):
    return render(request, 'packages/white_car.html')

def elegant_coctail_cresses(request):
    return render(request, 'packages/elegant_coctail_cresses.html')

def bridal_saree(request):
    return render(request, 'packages/bridal_saree.html')

def bridal_lahenga(request):
    return render(request, 'packages/bridal_lahenga.html')

def formal_dresses(request):
    return render(request, 'packages/formal_dresses.html')

def groom_panjabi(request):
    return render(request, 'packages/panjabi.html')

def photographer(request):
    return render(request, 'packages/photographer.html')

def cinemetography(request):
    return render(request, 'packages/cinemetography.html')

def projector(request):
    return render(request, 'packages/projector.html')