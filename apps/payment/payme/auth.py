import base64 
import binascii

from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.authentication import get_authorization_header

from apps.payment.payme.utils import get_credentials


def authentication(request):
    auth = get_authorization_header(request).split()

    if not auth or auth[0].lower() != b'basic':
        return False
    
    if len(auth) != 2:
        return False
    
    try:
        auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(":")
    except (TypeError, UnicodeDecodeError, binascii.Error):
        return False

    user_id, password = auth_parts[0], auth_parts[2]
    credentials = get_credentials()
    

    secret_key = credentials['PAYME_SECRET_KEY']
    test_secret_key = credentials['PAYME_TEST_SECRET_KEY']
    in_app_secret_key = credentials['PAYME_IN_APP_SECRET_KEY']
    in_app_test_secret_key = credentials['PAYME_IN_APP_TEST_SECRET_KEY']

    return (user_id == 'Paycom' and 
            (password == secret_key or password == test_secret_key or password == in_app_secret_key or password == in_app_test_secret_key))
