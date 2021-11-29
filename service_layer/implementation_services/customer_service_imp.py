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
            if current_customer.customer_id == customer.customer_id or current_customer.user_name == customer.user_name:
                raise DuplicateCustomerException("This account already exists")
            else:
                return self.customer_dao.create_customer_entry(customer)

    def get_customer_balance_by_id(self, customer_id: str, account_id: int) -> int:
        pass

    def deposit_into_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        pass

    def withdraw_from_account_by_id(self, customer_id: str, account_id: int, amount: int) -> int:
        pass

    def transfer_money_by_their_ids(self, customer_id: str, from_account_id: int, to_account_id: int,
                                    amount: int) -> int:
        pass

    def update_customer_by_id(self, customer_id: str, customer: Customer) -> Customer:
        pass

    def get_customer_by_id(self, customer_id: str) -> Customer:
        pass

    def delete_account_by_id(self, customer_id: str, account_id: int) -> bool:
        pass

    def delete_customer_by_id(self, customer_id: str) -> bool:
        pass

