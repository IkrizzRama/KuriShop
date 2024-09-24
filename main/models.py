from django.db import models
import uuid
from django.contrib.auth.models import User



class objectEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    object = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.object
# Create your models here.
