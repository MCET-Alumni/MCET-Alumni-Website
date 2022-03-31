''' Alumni model to store the information about alumni.'''

from email.policy import default
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
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
    ('ee', 'Electrical Engineering'),
    ('it', 'Information Technology')
)

status_choices = (
    (str(1), 'Approved'),
    (str(2), 'Pending'),
    (str(3), 'Rejected'),
)

batch_choices = [(str(i),str(i)) for i in range(2002, 2022)]

class Alumni(models.Model):
    
    ''' Stores the alumni model information.'''

    batch = models.CharField(max_length=5, choices=batch_choices)
    department = models.CharField(max_length=5, choices=department_choices)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=gender_choices)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone1 = models.CharField(max_length=10, validators=[MaxLengthValidator(10)])
    phone2 = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=True, blank=True)
    current_location = models.TextField(null=True, blank=True)
    linked_url = models.CharField(max_length=50000, null=True, blank=True)
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

    # def save(self, *args, **kwargs):
    #     return super(*args, **kwargs)

    def __str__(self) -> str:
        ''' str representation for user object.'''

        return self.email

class Gallery(models.Model):
    batch = models.CharField(max_length=5, choices=batch_choices)
    photo = models.ImageField(
        upload_to = 'gallery/',
        validators = [validate_image_size],
        null = True,
        blank = True,
    )