from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('packages/', views.packages, name='packages'),
    path('online-booking/', views.online_booking, name='online_booking'),
    path('contact/', views.contact, name='contact'),
    path('online-booking/store_booking', views.store_booking, name='store_booking'),
    path('contact/store_contact', views.store_contact, name='store_contact'),

    # sub url of the packages url
    path('packages/venus/', views.venus, name='venus'),
    path('packages/photographer/', views.photographer, name='photographer'),
    path('packages/makeup_artists', views.makeup_artists, name='makeup_artists'),
    path('packages/mehendi_artists/', views.mehendi_artists, name='mehendi_artists'),
    path('packages/bridal_wear/', views.bridal_wear, name='bridal_wear'),
    path('packages/groom_wear/', views.groom_wear, name='groom_wear'),
    path('packages/kazi/', views.kazi, name='kazi'),
    path('packages/decorators/', views.decorators, name='decorators'),
    path('packages/caterers/', views.caterers, name='caterers'),
    path('packages/dj-and-live/', views.dj_and_live, name='dj_and_live'),
    path('packages/invite-card/', views.invite, name='invite'),
    path('packages/other-services/', views.other_services, name='other_services'),
    path('packages/other-services/dhaka/', views.dhaka_services, name='dhaka_service'),
    # sub routes of dhaka packages
    
    path('packages/other-services/dhaka/black_car', views.black_car, name='black_car'),
    path('packages/other-services/dhaka/white_car', views.white_car, name='white_car'),
    path('packages/other-services/dhaka/elegant_coctail_cresses', views.elegant_coctail_cresses, name='elegant_coctail_cresses'),
    path('packages/other-services/dhaka/bridal-saree', views.bridal_saree, name='bridal_saree'),
    path('packages/other-services/dhaka/bridal-lahenga', views.bridal_lahenga, name='bridal_lahenga'),
    path('packages/other-services/dhaka/formal-dresses', views.formal_dresses, name='formal_dresses'),
    path('packages/other-services/dhaka/groom-panjabi', views.groom_panjabi, name='groom_panjabi'),
    path('packages/other-services/dhaka/photographer', views.photographer, name='photographer'),
    path('packages/other-services/dhaka/cinemetography', views.cinemetography, name='cinemetography'),
    path('packages/other-services/dhaka/projector', views.projector, name='projector'),
    # chittagong sub routes
    path('packages/other-services/chittagong/', views.chittagong_services, name='chittagong_service'),

    path('packages/other-services/chittagong/black_car', views.black_car, name='black_car'),
    path('packages/other-services/chittagong/white_car', views.white_car, name='white_car'),
    path('packages/other-services/chittagong/elegant_coctail_cresses', views.elegant_coctail_cresses, name='elegant_coctail_cresses'),
    path('packages/other-services/chittagong/bridal-saree', views.bridal_saree, name='bridal_saree'),
    path('packages/other-services/chittagong/bridal-lahenga', views.bridal_lahenga, name='bridal_lahenga'),
    path('packages/other-services/chittagong/formal-dresses', views.formal_dresses, name='formal_dresses'),
    path('packages/other-services/chittagong/groom-panjabi', views.groom_panjabi, name='groom_panjabi'),
    path('packages/other-services/chittagong/photographer', views.photographer, name='photographer'),
    path('packages/other-services/chittagong/cinemetography', views.cinemetography, name='cinemetography'),
    path('packages/other-services/chittagong/projector', views.projector, name='projector'),


    path('packages/other-services/rajshahi/', views.rajshahi_services, name='rajshahi_service'),
    # rajshahi sub routes
    path('packages/other-services/rajshahi/black_car', views.black_car, name='black_car'),
    path('packages/other-services/rajshahi/white_car', views.white_car, name='white_car'),
    path('packages/other-services/rajshahi/elegant_coctail_cresses', views.elegant_coctail_cresses, name='elegant_coctail_cresses'),
    path('packages/other-services/rajshahi/bridal-saree', views.bridal_saree, name='bridal_saree'),
    path('packages/other-services/rajshahi/bridal-lahenga', views.bridal_lahenga, name='bridal_lahenga'),
    path('packages/other-services/rajshahi/formal-dresses', views.formal_dresses, name='formal_dresses'),
    path('packages/other-services/rajshahi/groom-panjabi', views.groom_panjabi, name='groom_panjabi'),
    path('packages/other-services/rajshahi/photographer', views.photographer, name='photographer'),
    path('packages/other-services/rajshahi/cinemetography', views.cinemetography, name='cinemetography'),
    path('packages/other-services/rajshahi/projector', views.projector, name='projector'),
]
