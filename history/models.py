from django.db import models

# Create history Url model


class HistoryUrl(models.Model):
    url = models.CharField(max_length=50)
