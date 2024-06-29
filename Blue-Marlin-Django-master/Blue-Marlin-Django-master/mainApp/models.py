from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField()

    def order_info(self):
        return self.name + "'s order info."

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    details = models.TextField()

    def show_info(self):

        return "click to check " + self.email + "'s information"
