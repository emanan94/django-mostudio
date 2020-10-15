from django.db import models

# Create your models here.

class Portrait(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='gallery/')
    #portrait_link=models

    class Meta:
        ordering=['-id']


    def __str__(self):
        return str(self.title)

