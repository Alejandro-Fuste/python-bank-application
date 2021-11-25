from abc import ABC, abstractmethod

from entities.customers import Customer


class CustomerDao(ABC):

    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_balance_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, customer_id: int, amount: int) -> Customer:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, customer_id: int, amount: int) -> Customer:
        pass

    @abstractmethod
    def transfer_money_by_their_ids(self, from_account_id: int, to_account_id: int, amount: int) -> Customer:
        pass

    @abstractmethod
    def update_customer_by_id(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def delete_account_by_id(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
