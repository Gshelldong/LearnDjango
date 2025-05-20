import os

from django.test import TestCase

# Create your tests here.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day54.settings')

import django
django.setup()

from app01 import models