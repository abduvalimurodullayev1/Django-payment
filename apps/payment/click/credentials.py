from typing import Tuple, Optional
from apps.payment.models import Providers
import os
import environ
from django.conf import settings

env = environ.Env()
env.read_env(os.path.join(settings.BASE_DIR, ".env"))


def get_credentials() -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    """
    Get ClickUP API credentials.

    This function retrieves the Paylov API credentials (API key, username, password, subscription key)
    from the database.

    Returns:
        Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]: A tuple containing Paylov API credentials.
            - CLICK_SECRET_KEY: The Secret API key for ClickUP.
            - CLICK_MERCHANT_ID: The merchant ID.
            - CLICK_MERCHANT_SERVICE_ID: The merchant service ID.
            - CLICK_REDIRECT_URL: Redirect URL.
    """

    CLICK = Providers.objects.filter(provider=Providers.ProviderChoices.CLICK, is_active=True)
    CLICK_SECRET_KEY = getattr(CLICK.filter(key="CLICK_SECRET_KEY").last(), "value", None)
    CLICK_MERCHANT_ID = getattr(CLICK.filter(key="CLICK_MERCHANT_ID").last(), "value", None)
    CLICK_MERCHANT_SERVICE_ID = getattr(CLICK.filter(key="CLICK_MERCHANT_SERVICE_ID").last(), "value", None)
    CLICK_MERCHANT_USER_ID = getattr(CLICK.filter(key="CLICK_MERCHANT_USER_ID").last(), "value", None)
    CLICK_REDIRECT_URL = env.str("CLICK_REDIRECT_URL")
    CLICK_IN_APP_SECRET_KEY = getattr(CLICK.filter(key="CLICK_IN_APP_SECRET_KEY").last(), "value", None)

    return {
        "CLICK_SECRET_KEY": CLICK_SECRET_KEY,
        "CLICK_MERCHANT_ID": CLICK_MERCHANT_ID,
        "CLICK_MERCHANT_SERVICE_ID": CLICK_MERCHANT_SERVICE_ID,
        "CLICK_MERCHANT_USER_ID": CLICK_MERCHANT_USER_ID,
        "CLICK_REDIRECT_URL": CLICK_REDIRECT_URL,
        "CLICK_IN_APP_SECRET_KEY": CLICK_IN_APP_SECRET_KEY,
    }
