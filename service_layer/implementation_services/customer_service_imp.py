from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException
from data_access_layer.implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.customers import Customer
from service_layer.abstract_services.customer_service import CustomerService


class CustomerServiceImp(CustomerService):
    def __init__(self, customer_dao: CustomerDaoImp):
        self.customer_dao = customer_dao

    def create_customer_entry(self, customer: Customer) -> Customer:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.user_name == customer.user_name:
                raise DuplicateCustomerException("That account has already been created")
            else:
                return self.customer_dao.create_customer_entry(customer)

    def get_customer_balance_by_id(self, customer_id: str, account_id: int) -> int:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer_id:
                if current_customer.accounts.get(account_id) is None:
                    raise CustomerNotFoundException("This account was not found")
        return self.customer_dao.get_customer_balance_by_id(customer_id, account_id)

    def deposit_into_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer_id:
                if amount < 0:
                    raise InvalidTransactionException("This is not a valid transaction")
        return self.customer_dao.deposit_into_account_by_id(customer_id, account_id, amount)

    def withdraw_from_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer_id:
                if amount > current_customer.accounts[account_id]["balance"]:
                    raise InvalidTransactionException("This is not a valid transaction")
        return self.customer_dao.withdraw_from_account_by_id(customer_id, account_id, amount)

    def transfer_money_by_their_ids(self, customer_id: str, from_account_id: int, to_account_id: int,
                                    amount: int) -> int:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer_id:
                if amount > current_customer.accounts[from_account_id]["balance"]:
                    raise InvalidTransactionException("This is not a valid transaction")
        return self.customer_dao.transfer_money_by_their_ids(customer_id, from_account_id, to_account_id, amount)

    def update_customer_by_id(self, customer_id: str, customer: Customer) -> Customer:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer_id:
                return self.customer_dao.update_customer_by_id(customer_id, customer)
        raise CustomerNotFoundException("This account was not found")

    def get_customer_by_id(self, customer_id: str) -> Customer:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer_id:
                return self.customer_dao.update_customer_by_id(customer_id)
        raise CustomerNotFoundException("This account was not found")

    def delete_account_by_id(self, customer_id: str, account_id: int) -> bool:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer_id:
                if current_customer.accounts.get(account_id) is None:
                    raise CustomerNotFoundException("This account was not found")
        return self.customer_dao.delete_account_by_id(customer_id, account_id)

    def delete_customer_by_id(self, customer_id: str) -> bool:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer_id:
                return self.customer_dao.delete_customer_by_id(customer_id)
        raise CustomerNotFoundException("This account was not found")
