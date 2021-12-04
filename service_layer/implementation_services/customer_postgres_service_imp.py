from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException
from data_access_layer.implementation_classes.customer_postgres_dao_imp import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.abstract_services.customer_service import CustomerService
from typing import List


class CustomerPostgresServiceImp(CustomerService):
    def __init__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    def service_create_customer_entry(self, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customers()
        for current_customer in customers:
            if current_customer.user_name == customer.user_name:
                raise DuplicateCustomerException("That account has already been created")
        created_customer = self.customer_dao.create_customer_entry(customer)
        return created_customer

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        customers = self.customer_dao.get_all_customers()
        for current_customer in customers:
            if current_customer.customer_id == customer_id:
                return self.customer_dao.get_customer_by_id(customer_id)
            raise CustomerNotFoundException("This customer was not found")

    def service_get_all_customers(self) -> List[Customer]:
        return self.customer_dao.get_all_customers()

    def service_get_customer_balance_by_id(self, customer_id: int, account_id: int) -> float:
        balance = self.customer_dao.get_customer_balance_by_id(customer_id, account_id)
        if balance is None:
            raise CustomerNotFoundException("This account was not found")
        return balance

    def service_deposit_into_account_by_id(self, customer_id: int, account_id: int, amount: float) -> float:
        if amount <= 0:
            raise InvalidTransactionException("This is not a valid transaction")
        return self.customer_dao.deposit_into_account_by_id(customer_id, account_id, amount)

    def service_withdraw_from_account_by_id(self, customer_id: int, account_id: int, amount: float) -> float:
        balance = self.customer_dao.get_customer_balance_by_id(customer_id, account_id)
        float_balance = float('.'.join(str(elem) for elem in balance))
        if amount > float_balance:
            raise InvalidTransactionException("This is not a valid transaction")
        return self.customer_dao.withdraw_from_account_by_id(customer_id, account_id, amount)

    def service_transfer_money_by_their_ids(self, customer_id: int, from_account_id: int, to_account_id: int,
                                            amount: float) -> float:
        balance = self.customer_dao.get_customer_balance_by_id(customer_id, from_account_id)
        float_balance = float('.'.join(str(elem) for elem in balance))
        if amount > float_balance:
            raise InvalidTransactionException("This is not a valid transaction")
        return self.customer_dao.transfer_money_by_their_ids(customer_id, from_account_id, to_account_id, amount)

    def service_update_customer_by_id(self, customer_id: int, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customers()
        for customer in customers:
            if customer.customer_id == customer_id:
                return self.customer_dao.update_customer_by_id(customer_id, customer)
        raise CustomerNotFoundException("This account was not found")

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        customers = self.customer_dao.get_all_customers()
        for customer in customers:
            if customer.customer_id == customer_id:
                return self.customer_dao.delete_customer_by_id(customer_id)
        raise CustomerNotFoundException("This account was not found")
