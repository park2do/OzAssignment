from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	is_business = models.BooleanField(default=False)
	pass



###
{
    "detail": "Method \"GET\" not allowed.",
    "email": "alse@alsd.com",
    "password": "alse@alsdom"
}
###