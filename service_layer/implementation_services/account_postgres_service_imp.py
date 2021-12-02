from typing import List

from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException
from data_access_layer.implementation_classes.account_postgres_dao_imp import AccountPostgresDAO
from entities.accounts import Account
from service_layer.abstract_services.account_service import AccountService


class AccountPostgresServiceImp(AccountService):
    def create_account(self, account: Account) -> Account:
        pass

    def get_all_customers(self) -> List[Account]:
        pass

    def get_all_accounts(self) -> List[Account]:
        pass

    def get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        pass