from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
import datetime


# Create your models here.
class DateTest(models.Model):
    test_name = models.CharField(max_length=100, null=True)
    test_persian_date = jmodels.jDateTimeField(default=datetime.fromisoformat(jdatetime.datetime.now().isoformat()))
