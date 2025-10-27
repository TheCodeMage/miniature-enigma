from django.db import models
from django.utils import timezone # (to fix timezone error)

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(default=0) # 9999999999 ထားခဲ့လည်း ရတယ်
    joined_date = models.DateField(default=timezone.now)

