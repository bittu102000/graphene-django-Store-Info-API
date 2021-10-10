from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=225)
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email_id = models.EmailField(max_length=225)
    def __str__(self):
        return self.name + "-" + str(self.id)

class Item(models.Model):
    name = models.CharField(max_length=225)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    discount = models.FloatField(null=True,blank=True)
    gst = models.PositiveIntegerField(default=0)
    
    def total_amount(self):
        sub_total = self.price*self.quantity + self.gst
        after_discount = sub_total-self.discount
        return after_discount

    def __str__(self):
        return self.name + "-" + str(self.id)
    


class Invoice(models.Model):
    buyer_name = models.CharField(max_length=225)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    buyer_phone_number = models.CharField(validators=[phone_regex], max_length=17)
    transaction_time = models.DateTimeField(default=now)
    items = models.ForeignKey(Item,on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.buyer_name+"-" + str(self.id)
    def total_invoice(self):
        return (self.items.total_amount()+54)
        
