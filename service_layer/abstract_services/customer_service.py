from abc import ABC, abstractmethod
from typing import List
from entities.customers import Customer


class CustomerService(ABC):

    @abstractmethod
    def service_create_customer_entry(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id: str) -> Customer:
        pass

    @abstractmethod
    def service_get_all_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def service_get_customer_balance_by_id(self, customer_id: str, account_id: int) -> int:
        pass

    @abstractmethod
    def service_deposit_into_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        pass

    @abstractmethod
    def service_withdraw_from_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        pass

    @abstractmethod
    def service_transfer_money_by_their_ids(self, customer_id: str, from_account_id: int,
                                    to_account_id: int, amount: int) -> int:
        pass

    @abstractmethod
    def service_update_customer_by_id(self, customer_id: str, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: str) -> bool:
        pass
