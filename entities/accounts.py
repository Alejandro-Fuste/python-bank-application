class Account:
    def __init__(self, account_id: int, account_type: str, amount: float, customer_id: int):
        self.account_id = account_id,
        self.account_type = account_type,
        self.amount = amount,
        self.customer_id = customer_id

    def make_customer_dictionary(self):
        return {
            "accountId": self.account_id,
            "accountType": self.account_type,
            "amount": self.amount,
            "customerId": self.customer_id,
        }

    def __str__(self):
        return "account ID: {}, account type: {}, amount: {}, customer ID: {}"\
            .format(self.account_id, self.account_type, self.amount, self.customer_id)


