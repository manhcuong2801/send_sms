from django.db import models
from apps.core.consts import DEFAULT_API_UID


class CommonInfo(models.Model):
    """Abstract model contains common Odoo columns"""

    create_uid = models.IntegerField(null=True, default=DEFAULT_API_UID)
    create_date = models.DateTimeField(auto_now_add=True)
    write_uid = models.IntegerField(null=True, default=DEFAULT_API_UID)
    write_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
