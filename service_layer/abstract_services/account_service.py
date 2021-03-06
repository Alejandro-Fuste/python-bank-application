from abc import ABC, abstractmethod
from typing import List
from entities.accounts import Account


class AccountService(ABC):

    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_get_all_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def service_get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        pass

    @abstractmethod
    def service_delete_account_by_id(self, customer_id: str, account_id: int) -> bool:
        pass
