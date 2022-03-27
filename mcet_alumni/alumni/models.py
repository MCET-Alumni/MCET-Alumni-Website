''' Alumni model to store the information about alumni.'''

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.contrib.auth.models import User

from .helpers import validate_image_size

gender_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'), 
)

department_choices = (
    ('cse', 'Computer Science and Engineering'),
    ('ece', 'Electrics and communication Engineering'),
    ('ce', 'Civil Engineering'),
    ('ee', 'Electrical Engineering') 
)

status_choices = (
    ('Approved', 'Approved'),
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
)

class Alumni(models.Model):
    
    ''' Stores the alumni model information.'''

    batch = models.IntegerField(validators=[MinValueValidator(1998)])
    department = models.CharField(max_length=5, choices=department_choices)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=gender_choices)
    email = models.EmailField(max_length=255)
    phone1 = models.CharField(max_length=10, validators=[MaxLengthValidator(10)])
    phone2 = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=True, blank=True)
    current_location = models.TextField(null=True, blank=True)
    social_site_url = models.CharField(max_length=50000, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',
                                    validators=[validate_image_size],
                                    null = True,
                                    blank = True,
                                    )
    status = models.CharField(max_length=15, choices=status_choices)
    add_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='user_added', editable=False)
    last_modified =models.DateField(auto_now=True)
    modified_by = models.ForeignKey(to = User, on_delete = models.DO_NOTHING, related_name='user_modifies')

    class Meta:
        db_table = 'user'

    def __str__(self) -> str:
        ''' str representation for user object.'''

        return self.email