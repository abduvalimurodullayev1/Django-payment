import hashlib

from django.conf import settings
from apps.payment.click.credentials import get_credentials


def authentication(request):
    """
    Authentication function for click prepare and complete endpoints.
    """

    click_trans_id = request.POST.get("click_trans_id", None)
    service_id = request.POST.get("service_id", None)
    order_id = request.POST.get("merchant_trans_id", None)
    amount = request.POST.get("amount", None)
    action = request.POST.get("action", None)
    sign_time = request.POST.get("sign_time", None)
    sign_string = request.POST.get("sign_string", None)
    merchant_prepare_id = request.POST.get("merchant_prepare_id", None) if action == "1" else ""
    credentials = get_credentials()
    if order_id.isdigit():
        secret_key = credentials["CLICK_SECRET_KEY"]
    else:
        secret_key = credentials["CLICK_IN_APP_SECRET_KEY"]

    token = "{}{}{}{}{}{}{}{}".format(
        click_trans_id,
        service_id,
        secret_key,
        order_id,
        merchant_prepare_id,
        amount,
        action,
        sign_time,
    )

    encoder = hashlib.md5(token.encode("utf-8"))
    token = encoder.hexdigest()

    if token != sign_string:
        return False

    return True
