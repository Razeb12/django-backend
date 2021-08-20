from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job
from PIL import Image
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user=  models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    number= models.CharField(max_length=15)
    web= models.CharField(max_length=15,default=1)
    address= models.CharField(max_length=15,default=1)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        super().save(force_insert,force_update,using,update_fields)
        
        img= Image.open(self.image.path)
        
        if img.height>500 and img.width>500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Candidate(models.Model):
    first_name 			= models.CharField(max_length=20,null=False)
    last_name 			= models.CharField(max_length=15,null=False)
    phone 				= models.CharField(max_length=15,null=False)
    email_address 		= models.EmailField(max_length=40,null=False)
    zip_code 			= models.CharField(max_length=6,null=False)
	#SECONDARY VALUES (blank=True)
    linkedin 			= models.URLField(null=True, blank=True)
    resume 				= models.FileField('resume',upload_to='resumes/',default=None,null=True,blank=True)
    writeup 			= models.TextField('writeup',max_length=4000,default=None,null=True,blank=True)
    salary_base 		= models.IntegerField('base',default=100,null=True,blank=True)
    salary_bonus 		= models.IntegerField('bonus', default=20, null=True, blank=True)
    pub_date 			= models.DateTimeField('date published')
    job 				= models.ForeignKey(Job, on_delete=models.CASCADE,related_name='candidates')
	#interviews			= models.OneToManyField(Interview, blank=True)