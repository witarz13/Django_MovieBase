from django.db import models
class Movie(models.Model):
    title=models.CharField(max_length=220)
    year=models.IntegerField()
    url=models.CharField(max_length=220,null=True)
    info=models.CharField(max_length=2200,null=True)
    
    def __str__(self):
        return f'{self.title}'