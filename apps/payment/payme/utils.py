from apps.payment.models import Providers
import os
import environ
from django.conf import settings

env = environ.Env()
env.read_env(os.path.join(settings.BASE_DIR, ".env"))


def get_credentials():
    PAYME = Providers.objects.filter(provider=Providers.ProviderChoices.PAYME, is_active=True)
    PAYME_SECRET_KEY = env.str("PAYME_SECRET_KEY")
    PAYME_KASSA_ID = env.str("PAYME_KASSA_ID")
    PAYME_TEST_SECRET_KEY = env.str("PAYME_TEST_SECRET_KEY")
    PAYME_FIELD_NAME_FOR_ID = env.str("PAYME_FIELD_NAME_FOR_ID")
    PAYME_REDIRECT_URL = env.str("PAYME_REDIRECT_URL")
    PAYME_IN_APP_SECRET_KEY = env.str("PAYME_IN_APP_SECRET_KEY")
    PAYME_IN_APP_TEST_SECRET_KEY = env.str("PAYME_IN_APP_TEST_SECRET_KEY")
    PAYME_REDIRECT_URL = env.str("PAYME_REDIRECT_URL")
    return
