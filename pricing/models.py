from django.db import models

# Create your models here.

class Pricing(models.Model):
    image= models.ImageField(upload_to='pricing/')
    photography= models.ForeignKey('Photography', related_name='pricing_photography',on_delete=models.CASCADE)
    photos=models.ForeignKey('Photography', related_name='pricing_photos',on_delete=models.CASCADE)
    processing= models.ForeignKey('Photography', related_name='pricing_processing',on_delete=models.CASCADE)
    type_of_camera=models.ForeignKey('Photography', related_name='pricing_typeofcameray',on_delete=models.CASCADE)
    resolution= models.ForeignKey('Photography', related_name='pricing_resolution',on_delete=models.CASCADE)
    term= models.ForeignKey('Photography', related_name='pricing_term',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Pricing'

    def __str__(self):
        return str(self.photography)


#PhotographyType
class Photography(models.Model):
    photography=models.CharField(max_length=25)

    class Meta:
        verbose_name_plural='Photography'

    def __str__(self):
        return str(self.photography)

#photos
class Photos(models.Model):
    photo=models.CharField(max_length=20)


    class Meta:
        verbose_name_plural='Photos'

    def __str__(self):
        return str(self.photo)

#processing
class Processing(models.Model):
    processing=models.CharField(max_length=20)



    def __str__(self):
        return str(self.processing)


#type_of_camera
class TypeOfCamera(models.Model):
    type_of_camera=models.CharField(max_length=20)


    class Meta:
        verbose_name_plural='TypeOfCamera'

    def __str__(self):
        return str(self.type_of_camera)



#resolution
class Resolution(models.Model):
    resolution=models.CharField(max_length=20)

    class Meta:
        verbose_name_plural='Resolution'

    def __str__(self):
        return str(self.resolution)

#term
class Term(models.Model):
    term= models.IntegerField(default=0)


    def __str__(self):
        return str(self.term)