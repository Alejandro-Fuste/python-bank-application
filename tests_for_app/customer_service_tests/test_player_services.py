from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException
from data_access_layer.implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.customers import Customer
from service_layer.implementation_services.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDaoImp()
customer_service = CustomerServiceImp(customer_dao)
customer = Customer("Luke", "Skywalker", "Master Luke", "1", {1: {"type": "checking", "balance": 100},
                                                              2: {"type": "saving", "balance": 1000}})
customer_duplicate = Customer("Luke", "Skywalker", "Master Luke", "1", {1: {"type": "checking", "balance": 100},
                                                                        2: {"type": "saving", "balance": 1000}})


def test_validate_create_customer_method():
    try:
        customer_service.create_customer_entry(customer)
        assert False
    except DuplicateCustomerException as e:
        assert str(e) == "That account has already been created"


def test_validate_update_customer_method():
    try:
        customer_service.update_customer_by_id('1', customer_duplicate)
        assert False
    except DuplicateCustomerException as e:
        assert str(e) == "That username has already been taken"


def test_validate_deposit_method():
    try:
        pass
    except InvalidTransactionException as e:
        assert str(e) == "This transaction can not be completed"


def test_validate_withdraw_method():
    try:
        pass
    except InvalidTransactionException as e:
        assert str(e) == "This transaction can not be completed"


def test_validate_transfer_method():
    try:
        pass
    except InvalidTransactionException as e:
        assert str(e) == "This transaction can not be completed"


def test_validate_get_balance_method():
    try:
        pass
    except CustomerNotFoundException as e:
        assert str(e) == "This customer was not found"


def test_validate_get_customer_method():
    try:
        pass
    except CustomerNotFoundException as e:
        assert str(e) == "This customer was not found"


def test_validate_delete_account_method():
    try:
        pass
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"


def test_validate_delete_customer_method():
    try:
        pass
    except CustomerNotFoundException as e:
        assert str(e) == "This customer was not found"
