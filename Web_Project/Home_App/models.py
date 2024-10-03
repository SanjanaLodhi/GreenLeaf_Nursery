from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Island','Andaman & Nicobar Island'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Asam','Asam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Delhi','Delhi'),
    ('Madhya Predesh','Madhya Predesh'),
)

CATEGORY_CHOICES=(
    ('RS','Flower'),
    ('DP','Decorative Plant'),
    ('FP','Fruit Plant'),
)



class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=9)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
       return self.qunatity * self.product.discount_price