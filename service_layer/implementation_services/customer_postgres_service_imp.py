from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException
from data_access_layer.implementation_classes.customer_postgres_dao_imp import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.abstract_services.customer_service import CustomerService


class CustomerPostgresServiceImp(CustomerService):
    def __int__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    def create_customer_entry(self, customer: Customer) -> Customer:
        # customers = self

    def get_customer_balance_by_id(self, customer_id: int, account_id: int) -> float:
        # customers = self.customer_dao.

    def deposit_into_account_by_id(self, customer_id: int, account_id: int, amount: int) -> float:
        pass

    def withdraw_from_account_by_id(self, customer_id: int, account_id: int, amount: int) -> float:
        pass

    def transfer_money_by_their_ids(self, customer_id: int, from_account_id: int, to_account_id: float,
                                    amount: int) -> int:
        pass

    def update_customer_by_id(self, customer_id: int, customer: Customer) -> Customer:
        pass

    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    def delete_account_by_id(self, customer_id: int, account_id: int) -> bool:
        pass

    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
