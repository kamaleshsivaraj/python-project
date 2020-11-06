
# import os

from django-allauth.socailaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocailLoginView


class GoogleLogin(SocailLoginView):
    # """
    # docstring
    # """
    # pass

    adapter_class = GoogleOAuth2Adapter