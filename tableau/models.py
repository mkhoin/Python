from django.db import models

# Create your models here.

class email(models.Model):
    email = models.EmailField(max_length=70)

    def __str__(self): #
        return self.email


class image(models.Model):
    email = models.EmailField(max_length=70)
    image1=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image2=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image3=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __str__(self):  #
        return self.email
