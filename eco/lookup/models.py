from django.db import models
from datetime import datetime  
from django.utils import timezone
from django.contrib.auth.models import User

class siteInfo(models.Model):
    siteName = models.CharField(max_length=200)
    siteLogo = models.ImageField(upload_to='logo')
    Address = models.CharField(max_length=500)
    helpLine = models.CharField(max_length=200)
    email = models.CharField(max_length=100, default = None)
    topNotice = models.CharField(max_length=500)
    fbLink = models.CharField(max_length=200)
    twiterLink = models.CharField(max_length=200)
    LinkedinLink = models.CharField(max_length=200)
    supportDay =  models.IntegerField()
    supportHour =  models.IntegerField()
    siteDescription = models.CharField(max_length=500)
    aboutUs = models.CharField(max_length=500)
    privacyPolicy = models.CharField(max_length=800)
    deliveryInfomation = models.CharField(max_length=800)



class banner(models.Model):
    mainBanner =  models.ImageField(upload_to='banner')
    subBanner1 =  models.ImageField(upload_to='banner')
    subBanner2 =  models.ImageField(upload_to='banner')

class product(models.Model):
    id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=200)
    productImg =  models.ImageField(upload_to='productsImg')
    productImg2 =  models.ImageField(upload_to='productsImg', blank = True)
    productImg3 =  models.ImageField(upload_to='productsImg', blank = True)
    productCategories = models.CharField(max_length=200)
    productcolour = models.CharField(max_length=200)
    productPrice = models.IntegerField()
    productOffer = models.BooleanField(default=False)
    featuredproduct = models.BooleanField(default=False)
    OfferPercent = models.IntegerField()
    productDescription = models.CharField(max_length=500, default = 'fhdj fd')


