from django.db import models

# Create your models here.
class Todo(models.Model):
  task_id=models.IntegerField()
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=100)
  status=models.CharField(max_length=100)

  def __str__(self):
    return self.title