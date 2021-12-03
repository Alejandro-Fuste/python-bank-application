from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException
from data_access_layer.implementation_classes.customer_postgres_dao_imp import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.abstract_services.customer_service import CustomerService
from typing import List

class CustomerPostgresServiceImp(CustomerService):
    def __int__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    def service_create_customer_entry(self, customer: Customer) -> Customer:
        # customers = self

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    def service_get_all_customers(self) -> List[Customer]:
        pass

    def service_get_customer_balance_by_id(self, customer_id: int, account_id: int) -> float:
        # customers = self.customer_dao.

    def service_deposit_into_account_by_id(self, customer_id: int, account_id: int, amount: int) -> float:
        pass

    def service_withdraw_from_account_by_id(self, customer_id: int, account_id: int, amount: int) -> float:
        pass

    def service_transfer_money_by_their_ids(self, customer_id: int, from_account_id: int, to_account_id: float,
                                    amount: int) -> int:
        pass

    def service_update_customer_by_id(self, customer_id: int, customer: Customer) -> Customer:
        pass

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass
