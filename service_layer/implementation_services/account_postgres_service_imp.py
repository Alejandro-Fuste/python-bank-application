from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from data_access_layer.implementation_classes.account_postgres_dao_imp import AccountPostgresDAO
from entities.accounts import Account
from service_layer.abstract_services.account_service import AccountService
from typing import List


class AccountPostgresServiceImp(AccountService):
    def __init__(self, account_dao: AccountPostgresDAO):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        accounts = self.account_dao.get_all_accounts()
        for current_account in accounts:
            if current_account.account_type == account.account_type:
                raise DuplicateCustomerException("That account has already been created")
        created_account = self.account_dao.create_account(account)
        return created_account

    def service_get_all_accounts(self) -> List[Account]:
        return self.account_dao.get_all_accounts()

    def service_get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        accounts = self.account_dao.get_all_accounts()
        for current_account in accounts:
            if current_account.customer_id == customer_id:
                return self.account_dao.get_all_customer_accounts_by_id(customer_id)
        raise CustomerNotFoundException("This account was not found")

    def service_delete_account_by_id(self, customer_id: int, account_id: int) -> bool:
        accounts = self.account_dao.get_all_accounts()
        for current_account in accounts:
            if current_account.account_id == account_id:
                return self.account_dao.delete_account_by_id(customer_id, account_id)
        raise CustomerNotFoundException("This account was not found")

