from django.db import models

# Create your models here.

class email_info(models.Model):
    email_address = models.EmailField(max_length=70)

    def __str__(self): #
        return self.email_address


class image(models.Model):
    image1=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image2=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image3=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __str__(self):  #
        return self.image1
