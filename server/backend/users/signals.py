from django.db.models.signals import post_save
from django.dispatch import receiver

from allauth.socialaccount.models import socialaccount


def add_extra_data_to_user(sender, instance, created, *args, **kwargs):
    # """
    # docstring
    # """
    # pass

    instance.user.save()
    instance.user.avatar = instance.extra_data['picture']