class Account:
    def __init__(self, customer_id: str, account_id: int, account_type: str, amount: int):
        self.customer_id = customer_id,
        self.account_id = account_id,
        self.account_type = account_type,
        self.amount = amount

    def make_customer_dictionary(self):
        return {
            "customerId": self.customer_id,
            "accountId": self.account_id,
            "accountType": self.account_type,
            "amount": self.amount
        }

    def __str__(self):
        return "customer ID: {}, account ID: {}, account type: {}, amount: {}"\
            .format(self.customer_id, self.account_id, self.account_type, self.amount)



