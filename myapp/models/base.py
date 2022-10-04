import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # Ensure all saved objects are validated
    # https://www.cloudtruth.com/blog/self-validating-django-models
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
