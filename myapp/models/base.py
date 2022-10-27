import uuid
from django.db import models
#Time Zone
import datetime
#now = datetime.datetime.now()
from django.utils import timezone
#now = timezone.now(default=datetime.now)

# Time zone


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #modification
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # Ensure all saved objects are validated
    # https://www.cloudtruth.com/blog/self-validating-django-models
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
