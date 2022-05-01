from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=60)
    category_Image = models.ImageField(upload_to='categorypics', blank='True', null='True')

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    product_name= models.CharField(max_length=150)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    Image1 = models.ImageField(upload_to='productpics',blank='True',null='True')
    Image2 = models.ImageField(upload_to='productpics', blank='True', null='True')
    Image3 = models.ImageField(upload_to='productpics', blank='True', null='True')
    featured_product = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name