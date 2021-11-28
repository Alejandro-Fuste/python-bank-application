from typing import Dict
import uuid0


# def make_id():
#     return uuid0.generate()


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

# add method to create an account

# customer_1 = Customer("Luke", "Skywalker", "Master Jedi", 1,
#                       {1: {"type": "checking", "balance": 100},
#                        2: {"type": "saving", "balance": 1000}})
# customer_dict = customer_1.make_customer_dictionary()
# print(customer_1)
# print(customer_1.make_customer_dictionary())
# print(customer_dict['accounts']['1'])
# print(customer_dict['accounts']['2'])
# print(customer_1.accounts[1])
# id_id = str(make_id())
# print(id_id)
# print(type(id_id))
# print(len(id_id))
