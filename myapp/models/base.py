from django.db import models


class AbstractBaseModel(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # Ensure all saved objects are validated
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
