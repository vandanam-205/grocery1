from django.db import models

# Create your models here.
class userregistration(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    cpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.username


class registration(models.Model):
    username=models.CharField(max_length=50,null=False,blank=False)
    email=models.EmailField(max_length=50,null=False,blank=False)
    password=models.CharField(max_length=50,null=False,blank=False)
    cpassword=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.username
    
class category(models.Model):
    catname=models.CharField(max_length=50,null=False,blank=False)
    catimage=models.FileField(upload_to='img/')

    def __str__(self):
        return self.catname
    
class subcategory(models.Model):
    categoryid=models.ForeignKey(category,on_delete=models.CASCADE)
    categoryname=models.CharField(max_length=50,null=False,blank=False)
    categoryimage=models.FileField(upload_to='img/',default=None)
    def __str__(self):
        return self.categoryname
    
class product(models.Model):
    categoryid=models.ForeignKey(subcategory,on_delete=models.CASCADE)
    productname=models.CharField(max_length=50,null=False,blank=False)
    productimage=models.FileField(upload_to='img/',default=None)
    productdesc=models.TextField(max_length=50)
    productstock=models.IntegerField()
    productprice=models.IntegerField()

    def __str__(self):
        return self.productname
