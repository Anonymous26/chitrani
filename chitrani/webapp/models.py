from django.db import models

import datetime
import os
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDERS = (
        ('M', 'Male'),
    	('F', 'Female'),
    )
    name = models.CharField(max_length=200,blank=True, null=True) #We will place check on the front end
    gender = models.CharField(max_length=1, choices=GENDERS,blank=True, null=True) #Place check on the front end
    dob = models.DateField(null=True)	
    # email_id = models.EmailField(blank=True, null=True)
    profile_pic= models.ImageField(blank=True, upload_to='pictures', null=True)
    email_verified= models.BooleanField(default=False)    	
    created_at = models.DateTimeField( auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'Profiles'
    def __unicode__(self):
        return str(self.name)

