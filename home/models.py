from django.db import models

# Create your models here.
class Carousel_Data(models.Model):
    name=models.CharField(max_length=50 , default="Undefined")
    photo= models.ImageField(upload_to="home/images",default="")
    # def __str__(self):
    #     return nam
class loogin_data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100 ,default="abc@gmail.com")
    last_name = models.CharField(max_length=100)
    password1=models.IntegerField()
    password2=models.IntegerField()
    phone=models.IntegerField()
    def __str__(self):
        return self.name

class project_details(models.Model):
    heading = models.CharField(max_length=100)
    project_image= models.ImageField(upload_to="home/images",default="")
    project_descp = models.CharField(max_length=1000)
    project_link = models.CharField(max_length=100)
    def __str__(self):
        return self.heading