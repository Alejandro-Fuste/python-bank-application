from typing import List

from data_access_layer.abstract_classes.account_dao import AccountDao
from entities.accounts import Account
from util.database_connection import connection


class AccountPostgresDAO(AccountDao):

    def create_account(self, customer_id: int, account: Account) -> Account:
        pass

    def get_all_customers(self) -> List[Account]:
        pass

    def get_all_accounts(self) -> List[Account]:
        pass

    def get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        pass
