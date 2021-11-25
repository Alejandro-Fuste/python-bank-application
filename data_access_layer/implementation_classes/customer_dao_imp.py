from data_access_layer.abstract_classes.customer_dao import CustomerDao
from entities.customers import Customer


class CustomerDaoImp(CustomerDao):
    # starting instances
    customer_one = Customer("Luke", "Skywalker", "Master Luke", 1, {1: {"type": "checking", "balance": 100},
                                                                    2: {"type": "saving", "balance": 1000}})
    customer_two = Customer("Leia", "Organa", "Princess Leia", 2, {3: {"type": "checking", "balance": 100},
                                                                   4: {"type": "saving", "balance": 1000}})
    customer_to_delete = Customer("Anakin", "Skywalker", "Cancel Me", 3, {5: {"type": "checking", "balance": 100},
                                                                          6: {"type": "saving", "balance": 1000}})

    # "database" list
    customer_list = [customer_one, customer_two, customer_to_delete]

    # id generator
    customer_id_generator = 4

    # methods that perform bank actions
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    def get_customer_balance_by_id(self, customer_id: int) -> Customer:
        pass

    #     use get dictionary method...set second argument to zero
    def deposit_into_account_by_id(self, customer_id: int, amount: int) -> Customer:
        pass

    def withdraw_from_account_by_id(self, customer_id: int, amount: int) -> Customer:
        pass

    def transfer_money_by_their_ids(self, from_account_id: int, to_account_id: int, amount: int) -> Customer:
        pass

    def update_customer_by_id(self, customer: Customer) -> Customer:
        pass

    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    def delete_account_by_id(self, customer_id: int) -> bool:
        pass

    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
