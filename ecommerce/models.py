from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ('BAGMATI', 'BAGMATI'),
    ('GANDAKI', 'GANDAKI'),
    ('LUMBINI', 'LUMBINI'),
    ('KARNALI ', 'KARNALI'),
    ('SUDHURPASCHIM ', 'SUDHURPASCHIM'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (

    ('F', 'FULLFACE'),
    ('H', 'Halfface'),
    ('B', 'BOOTS'),
    ('W', 'WEARS'),
    
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)



STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delievered', 'Delievered'),
    ('Cancel', 'Cancel')
)






class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

    @property
    def total_amount(self):

        return (self.quantity * self.product.discounted_price)+100

    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Profile(models.Model):
    user=models.OneToOneField(User, null =True, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10,null=True)
    username=models.CharField(max_length=200,null=True)
    email=models.EmailField()
    profile_pic=models.FileField(upload_to='static/userimage',default='static/userimage/usericon.png')
    created_date=models.DateTimeField(auto_now_add=True)
