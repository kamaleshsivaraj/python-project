from django .contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # """
    # docstring
    # """

    photo = models.URLField(blank=True)

    def _str_(self):
        # """
        # docstring
        # """
        return self.username