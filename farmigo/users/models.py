from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BaseUser(AbstractUser):
    USER_TYPE = (
        ('FMR', 'Farmer'),
        ('SPR', 'Supplier'),
        ('RTR', 'Retailer'),
    )
    user_type = models.CharField(max_length=3, choices=USER_TYPE, default='FMR')
    username = models.CharField(max_length=10, null=False, blank=False, unique=True)
    mobnumber = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        self.mobnumber = self.username
        super(BaseUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "BaseUser"
        verbose_name_plural = "BaseUsers"

class Farmer(models.Model):
    baseuser = models.OneToOneField(BaseUser, related_name='farmer', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    loc_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    loc_long = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    op_land_area = models.DecimalField(max_digits=5, decimal_places=2)
    dob = models.DateField(verbose_name='date_of_birth', name='dob', null=True)
    address = models.CharField(max_length=64, null=True, blank=True)
    town = models.CharField(max_length=64, null=True, blank=True)
    district = models.CharField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Crop(models.Model):
    farmer = models.ForeignKey(Farmer, related_name="crop", on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=32)
    crop_type = models.CharField(max_length=32)

    def __str__(self):
        return self.crop_name

class FarmerProduct(models.Model):
    PRODUCT_TYPE = (
        ('CP', 'Crop Product'),
        ('AP', 'Animal Product'),
    )
    farmer = models.ForeignKey(Farmer, related_name="farmer_product", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    quality_index = models.FloatField()
    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE, default='CP')

    def __str__(self):
        return self.product_name

class Livestock(models.Model):
    farmer = models.ForeignKey(Farmer, related_name="livestock", on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    age = models.IntegerField()

    def __str__(self):
        return self.name


#Retailer
class Retailer(models.Model):
    baseuser = models.OneToOneField(BaseUser, related_name='retailer', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    shop_location = models.FloatField(null=True)

    def __str__(self):
        return self.shop_name


class RetailerProduct(models.Model):
    retailer = models.ForeignKey(Retailer, related_name='retailer_product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    product_price = models.FloatField()

    def __str__(self):
        return self.product_name


#Supplier
class Supplier(models.Model):
    baseuser = models.ForeignKey(BaseUser, related_name='supplier', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, related_name='supplier_product', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    product_price = models.FloatField()

    def __str__(self):
        return self.name



