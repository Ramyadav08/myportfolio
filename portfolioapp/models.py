from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()
    
    def __str__(self):
        return self.name 


class Blogs(models.Model):
    title=models.CharField(max_length=250,default=0)
    projecturl = models.URLField(default='https://www.linkedin.com/in/ramrekha-yadav-4a8b21251/')
    img=models.ImageField(upload_to='blog',blank=True,null=True,default=0)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.title 