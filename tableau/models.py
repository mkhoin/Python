from django.db import models

# Create your models here.
class image(models.Model):
    image1=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image2=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image3=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __unicode__(self):  #
        return self.id
