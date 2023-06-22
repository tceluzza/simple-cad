from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Officer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    radio_id = models.CharField(max_length=32)
    active_call = models.ForeignKey(
            "Call",
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
    )
    vehicle = models.ForeignKey(
            "Vehicle", 
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
    )   

    @admin.display(
            ordering="radio_id",
    )

    def get_name(self):
        name_string = "{}. {}"
        return name_string.format(self.first_name[0], self.last_name)

    def __str__(self):
        name_string = "{} ({})"
        return name_string.format( self.get_name(), self.radio_id )

class Vehicle(models.Model):
    name = models.CharField(max_length=32)
    variety = models.CharField(max_length=32)
    radio_id = models.CharField(max_length=4)
    license_plate = models.OneToOneField(
        "LicensePlate",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class LicensePlate(models.Model):
    MUNICIPAL_VEHICLE="MVN"
    MUNICIPAL_MOTORCYCLE="MXN"
    PASSENGER_NORMAL="PAN"

    PLATE_TYPE_CHOICES = [
        (
            "Municipal",
            (
                (MUNICIPAL_VEHICLE, "Municipal Vehicle"),
                (MUNICIPAL_MOTORCYCLE, "Municipal Motorcycle"),
            ),
        ),
        (
            "Passenger",
            (
                (PASSENGER_NORMAL, "Passenger Normal"),
            ),
        ),
        ("XXX", "Unknown"),
    ]

    plate_type = models.CharField(
            max_length=3,
            choices=PLATE_TYPE_CHOICES,
            default=MUNICIPAL_VEHICLE,
    )

    plate_number = models.CharField(max_length=8)

    def __str__(self):
        return self.plate_number

class Call(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
