class ClickUpClient:
    def __init__(self, data):
        self.data = data
        self.client_trans_id = self.data.get("click_trans_id", None)
        self.service_id = self.data.get("service_id", None)
        self.click_paydoc_id = self.data.get("click_paydoc_id", None)
        self.order_id = self.data.get("merchant_trans_id", None)
        self.amount = self.data.get("amount", None)
        self.action = self.data.get("action", None)
        self.error = self.data.get("error", None)
        self.error_note = self.data.get("error_note", None)
        self.sign_time = self.data.get("sign_time", None)
        self.sign_string = self.data.get("sign_string", None)
        self.merchant_prepare_id = self.data.get("merchant_prepare_id", None) if self.action == 1 else ""
        self.order = self.get_order()
        self.success_response = {"error": "0", "error_note": "Success"}
        self.transaction_found = False
        self.transaction = None

    def prepare(self):
        if self.action != 0:
            return {"error": "-3", "error_note": "Action not found"}
        if not self.order:
            return {"error": "-5", "error_note": "Order does not exist"}

        check_order, error_response = self.check_order()
        if not check_order:
            return error_response

        can_prepare_transaction, error_response = self.can_prepare_transaction()
        if not can_prepare_transaction:
            return error_response

        is_valid_amount, error_response = self.is_valid_amount()
        if not is_valid_amount:
            return error_response

        return self.success_response
