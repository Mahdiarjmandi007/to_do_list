from django.db import models

class do_list (models.Model):
    titles = models.CharField(max_length=200)
    descriptions = models.TextField()
    statuss = models.BooleanField(default=False)
    s_date= models.DateTimeField(auto_now_add=True)
    e_date=models.DateTimeField(null=True,blank=True)
# Create your models here.
