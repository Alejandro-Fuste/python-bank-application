from typing import List

from data_access_layer.abstract_classes.account_dao import AccountDao
from entities.accounts import Account


class AccountDaoImp(AccountDao):
    # starting instances
    account_one = Account('1', 1, 'checking', 100)
    account_two = Account('1', 2, 'saving', 1000)
    account_three = Account('2', 3, 'checking', 100)
    account_four = Account('2', 4, 'saving', 1000)
    account_five = Account('3', 5, 'checking', 100)
    account_six = Account('3', 6, 'saving', 1000)

    # "database" list
    account_list = [account_one, account_two, account_three, account_four, account_five, account_six]

    # id generator
    customer_id_generator = 7

    def create_account(self, customer_id: int, account: Account) -> Account:
        pass

    def get_all_customers(self) -> List[Account]:
        pass

    def get_all_accounts(self) -> List[Account]:
        pass

    def get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        pass
