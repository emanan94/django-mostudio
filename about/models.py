from django.db import models

# Create your models here.


class CEO(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='about/')
    quotation=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='CEO'


    def __str__(self):
        return str(self.name)



class Team(models.Model):
    name=models.CharField(max_length=30)
    image= models.ImageField(upload_to='about/')
    position=models.ForeignKey('Position',related_name='team_position',on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural='Team'


    def __str__(self):
        return str(self.name)



class Position(models.Model):
    position= models.CharField(max_length=25)


    def __str__(self):
        return str(self.position)