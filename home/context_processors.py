from datetime import date
from django.utils import timezone
import datetime
from datetime import date
from .models import *
def base(request):
    month=date.today().strftime('%Y-%m')
    mon,created=Attendance_month.objects.get_or_create(month=month)
    if created:
        mon.save()
        print("create")
    else:
        print("error")
    pram={'emp':employee.objects.all()}
    return pram