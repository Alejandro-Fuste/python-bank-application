from typing import Dict


class Customer:
    def __init__(self, first_name: str, last_name: str, user_name: str, customer_id: int, accounts: Dict[str, Dict]):
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


# add method to create an account

# customer_1 = Customer("Luke", "Skywalker", "Master Jedi", 1,
#                       {"1": {"type": "checking", "balance": 100},
#                        "2": {"type": "saving", "balance": 1000}})
# customer_dict = customer_1.make_customer_dictionary()
# print(customer_1)
# print(customer_1.make_customer_dictionary())
# print(customer_dict['accounts']['1'])
# print(customer_dict['accounts']['2'])
