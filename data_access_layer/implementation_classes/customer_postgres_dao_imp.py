from data_access_layer.abstract_classes.customer_dao import CustomerDao
from util.database_connection import connection
from entities.customers import Customer


class CustomerPostgresDAO(CustomerDao):
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    def get_customer_balance_by_id(self, customer_id: str, account_id: int) -> int:
        pass

    def deposit_into_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        pass

    def withdraw_from_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        pass

    def transfer_money_by_their_ids(self, customer_id: str, from_account_id: int, to_account_id: int, amount: int) -> \
            int:
        pass

    def update_customer_by_id(self, customer_id: str, customer: Customer) -> Customer:
        pass

    def get_customer_by_id(self, customer_id: str) -> Customer:
        pass

    def delete_account_by_id(self, customer_id: str, account_id: int) -> bool:
        pass

    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
