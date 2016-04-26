from __future__ import unicode_literals

from django.db import models

PAYMENT_MODE =(
        ('CASH', 'Cash'),
        ('BANK DEPOSIT', 'Bank Deposit'),
        ('CHEQUE', 'Cheque'),
        ('RTGS', 'RTGS'),
    )

class Customer(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class Vehicle(models.Model):
    customer = models.ForeignKey(Customer)
    vehicle_make = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20, blank=True, null=True)
    vehicle_registration_number = models.CharField(max_length=20, blank=False, null=False, unique=True)
    vehicle_chasis_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    installation_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.vehicle_make + self.customer.name


class Payment(models.Model):
    customer = models.ForeignKey(Customer)
    mode_of_payment = models.CharField(max_length=20, choices=PAYMENT_MODE)
    name_payer = models.CharField(max_length=20, blank=True, null=True)
    account_name = models.CharField(max_length=20, blank=True, null=True)
    bank = models.CharField(max_length=20, blank=True, null=True)
    amount = models.IntegerField()
    amount_due = models.IntegerField(blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.customer.name + "-->" + str(self.amount)


class Invoice(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    amount = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.vehicle.customer.name + ': ' + str(self.amount)