from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Tasks(models.Model):
    id = models.AutoField(primary_key= True)
    task_name = models.CharField(max_length= 100)
    task_description = models.CharField(max_length= 500)
    task_start_date = models.DateField
    task_end_date = models.DateField
    task_work_start = models.BooleanField(default= False)
    task_completion_status = models.BooleanField(default= False)
    task_progress_status = models.PositiveSmallIntegerField(
        validators= [
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        help_text="'Enter a percentage value between 0 and 100 "
    )



