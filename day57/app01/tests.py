from django.test import TestCase

# Create your tests here.
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day57.settings')

import django
django.setup()

from app01 import models

res = models.User.objects.filter(pk=2).first() # type: models.User
print(res.get_gender_display())
