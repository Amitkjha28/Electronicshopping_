from django.contrib import admin

# Register your models here.
from myapp.models import Category, Subcategory, Product

# 1st Method
admin.site.register(Category)

# 2nd Method
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["subcategory_name",'category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name","price","discount","subcategory",'category']