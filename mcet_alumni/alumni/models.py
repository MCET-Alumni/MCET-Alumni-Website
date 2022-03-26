''' Alumni model to store the information about alumni.'''

import imp
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

from .helpers import validate_image_size

class Department(models.Model):
    name = models.CharField(max_length=100)

gender_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'), 
)

class Alumni(models.Model):
    
    ''' Stores the alumni model information.'''

    batch = models.IntegerField(validators=[MinValueValidator(1998)])
    department = models.ForeignKey(to='Department', on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=gender_choices)
    email = models.EmailField(max_length=255)
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='profile_pics/',
                                    validators=[validate_image_size],
                                    null = True,
                                    blank = True,
                                    )
    add_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='user_added')
    last_modified =models.DateField(auto_now=True)
    modified_by = models.ForeignKey(to = User, on_delete = models.DO_NOTHING, related_name='user_modifies')

    class Meta:
        db_table = 'user'

    def __str__(self) -> str:
        ''' str representation for user object.'''

        return self.email