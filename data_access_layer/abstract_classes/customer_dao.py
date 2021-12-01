from abc import ABC, abstractmethod
from typing import List
from entities.customers import Customer


class CustomerDao(ABC):

    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_balance_by_id(self, customer_id: str, account_id: int) -> int:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        pass

    @abstractmethod
    def transfer_money_by_their_ids(self, customer_id: str, from_account_id: int, to_account_id: int, amount: int) -> int:
        pass

    @abstractmethod
    def update_customer_by_id(self, customer_id: str, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: str) -> Customer:
        pass

    @abstractmethod
    def delete_account_by_id(self, customer_id: str, account_id: int) -> bool:
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def create_account(self, customer_id: int, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_all_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def get_all_accounts(self) -> List[Customer]:
        pass

    @abstractmethod
    def get_all_customer_accounts_by_id(self, customer_id: int) -> List[Customer]:
        pass
