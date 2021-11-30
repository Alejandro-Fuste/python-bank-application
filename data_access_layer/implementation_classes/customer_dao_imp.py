from data_access_layer.abstract_classes.customer_dao import CustomerDao
from entities.customers import Customer
import uuid0


class CustomerDaoImp(CustomerDao):
    # starting instances
    customer_one = Customer("Luke", "Skywalker", "Master Luke", "1", {1: {"type": "checking", "balance": 100},
                                                                      2: {"type": "saving", "balance": 1000}})
    customer_two = Customer("Leia", "Organa", "Princess Leia", "2", {3: {"type": "checking", "balance": 100},
                                                                     4: {"type": "saving", "balance": 1000}})
    customer_to_delete = Customer("Anakin", "Skywalker", "Cancel Me", "3", {5: {"type": "checking", "balance": 100},
                                                                            6: {"type": "saving", "balance": 1000}})

    # "database" list
    customer_list = [customer_one, customer_two, customer_to_delete]

    # id generator
    customer_id_generator = str(uuid0.generate())

    # methods that perform bank actions
    def create_customer_entry(self, customer: Customer) -> Customer:
        customer.customer_id = CustomerDaoImp.customer_id_generator
        CustomerDaoImp.customer_list.append(customer)
        return customer

    def get_customer_balance_by_id(self, customer_id: str, account_id: int) -> int:
        for customer in CustomerDaoImp.customer_list:
            if customer.customer_id == customer_id:
                return customer.accounts[account_id]['balance']

    def deposit_into_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        for customer in CustomerDaoImp.customer_list:
            if customer.customer_id == customer_id:
                balance = customer.accounts[account_id]['balance']
                new_balance = balance + amount
                customer.accounts[account_id]['balance'] = new_balance
                return new_balance

    def withdraw_from_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        for customer in CustomerDaoImp.customer_list:
            if customer.customer_id == customer_id:
                balance = customer.accounts[account_id]['balance']
                new_balance = balance - amount
                customer.accounts[account_id]['balance'] = new_balance
                return new_balance

    def transfer_money_by_their_ids(self, customer_id: str, from_account_id: int, to_account_id: int,
                                    amount: int) -> int:
        self.withdraw_from_account_by_id(customer_id, from_account_id, amount)
        self.deposit_into_account_by_id(customer_id, to_account_id, amount)
        return self.get_customer_balance_by_id(customer_id, to_account_id)

    def update_customer_by_id(self, customer_id: str, customer: Customer) -> Customer:
        for cust in CustomerDaoImp.customer_list:
            if cust.customer_id == customer_id:
                index = CustomerDaoImp.customer_list.index(cust)
                CustomerDaoImp.customer_list[index] = customer
                return customer

    def get_customer_by_id(self, customer_id: str) -> Customer:
        for customer in CustomerDaoImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def delete_account_by_id(self, customer_id: str, account_id: int) -> bool:
        for customer in CustomerDaoImp.customer_list:
            if customer.customer_id == customer_id:
                del customer.accounts[account_id]
                return True

    def delete_customer_by_id(self, customer_id: str) -> bool:
        for customer in CustomerDaoImp.customer_list:
            if customer.customer_id == customer_id:
                index = CustomerDaoImp.customer_list.index(customer)
                del CustomerDaoImp.customer_list[index]
                return True


new_cus = CustomerDaoImp()

# print(new_cus.withdraw_from_account_by_id('1', 1, 100))
# print(new_cus.get_customer_balance_by_id("1", 1))
# print(new_cus.transfer_money_by_their_ids('1', 2, 1, 100))
# print(new_cus.delete_account_by_id('3', 6))
# print(new_cus.delete_customer_by_id("3"))
# print(new_cus.customer_list)

# updated_info = Customer("Luke", "Skywalker", "master jedi", "1", {1: {"type": "checking", "balance": 100},
#                                                                   2: {"type": "saving", "balance": 1000}})
# print(new_cus.update_customer_by_id('1', updated_info))
print(new_cus.customer_list[0].customer_id)





