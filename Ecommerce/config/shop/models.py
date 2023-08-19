from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return self.title

class Item(models.Model):
    LABEL = (
        ('Speciall offer','speciall offer'),
        ('Best seller','best seller'),
        ('New','new')
    )
    GENDER = (
        ('F','female'),
        ('M','man')
    )
    name = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    label = models.CharField(max_length=14,choices=LABEL)
    gender =models.CharField(max_length=1,choices=GENDER)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)
    available = models.BooleanField(default=False)

    def __str__(self) :
        return self.name
    
class Order(models.Model):
    STATUS = (
        ("Paid","paid"),
        ("Unpaid","unpaid")
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    status = models.CharField(max_length=25,choices=STATUS)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return self.item

class CheckoutOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=300)
    adress = models.TextField()
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    name_on_card = models.CharField(max_length=250)
    credit_card_number = models.IntegerField()
    Expiration = models.DateField()
    CVV = models.IntegerField()
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return f"{self.order} for {self.first_name}{self.last_name}"