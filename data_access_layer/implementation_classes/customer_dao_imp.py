from abc import ABC, abstractmethod

from entities.customers import Customer


class CustomerDao(ABC):

    # create new customer method
    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_balance_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self, from_account_id: int, to_account_id: int) -> Customer:
        pass
