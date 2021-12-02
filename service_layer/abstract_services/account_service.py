from abc import ABC, abstractmethod
from typing import List
from entities.accounts import Account


class AccountDao(ABC):

    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_all_customers(self) -> List[Account]:
        pass

    @abstractmethod
    def get_all_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        pass
