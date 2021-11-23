from data_access_layer.abstract_classes.customer_dao import CustomerDao
from entities.customers import Customer


class CustomerDaoImp(CustomerDao):
    # add starting instances
    # add "database" list
    # add id generator

    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    def get_customer_balance_by_id(self, customer_id: int) -> Customer:
        pass

    def deposit_into_account_by_id(self, customer_id: int) -> Customer:
        pass

    def withdraw_from_account_by_id(self, customer_id: int) -> Customer:
        pass

    def transfer_money_between_accounts_by_their_ids(self, from_account_id: int, to_account_id: int) -> Customer:
        pass

    def update_customer_by_id(self, customer_id: int) -> Customer:
        pass

    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    def delete_account_by_id(self, customer_id: int) -> bool:
        pass

    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
