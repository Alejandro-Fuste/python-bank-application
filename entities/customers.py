from typing import Dict


class Customer:
    def __init__(self, first_name: str, last_name: str, user_name: str, customer_id: str, accounts: Dict[int, Dict]):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.customer_id = customer_id
        self.accounts = accounts

    def make_customer_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "userName": self.user_name,
            "customerId": self.customer_id,
            "accounts": self.accounts
        }

    def __str__(self):
        return "first name: {}, last name: {}, username: {}, " \
               "customer ID: {}, accounts: {}".format(self.first_name, self.last_name,
                                                      self.user_name, self.customer_id, self.accounts)



