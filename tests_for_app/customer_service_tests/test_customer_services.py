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
customer_update = Customer("Luke", "Skywalker", "I am not the father", "1", {1: {"type": "checking", "balance": 100},
                                                                             2: {"type": "saving", "balance": 1000}})
customer_two = Customer("Rey", "NoLastName", "skywalker", "5",
                        {7: {"type": "checking", "balance": 100},
                         8: {"type": "saving", "balance": 1000}})


def test_validate_create_customer_method():
    try:
        customer_service.create_customer_entry(customer)
        assert False
    except DuplicateCustomerException as e:
        assert str(e) == "That account has already been created"


def test_validate_get_balance_method():
    try:
        customer_service.get_customer_balance_by_id('1', 4)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"


def test_validate_deposit_method():
    try:
        customer_service.deposit_into_account_by_id('1', 1, -100)
        assert False
    except InvalidTransactionException as e:
        assert str(e) == "This is not a valid transaction"


def test_validate_withdraw_method():
    try:
        customer_service.withdraw_from_account_by_id('1', 1, 2000)
        assert False
    except InvalidTransactionException as e:
        assert str(e) == "This is not a valid transaction"


def test_validate_transfer_method():
    try:
        customer_service.transfer_money_by_their_ids('1', 2, 1, 2000)
        assert False
    except InvalidTransactionException as e:
        assert str(e) == "This is not a valid transaction"


def test_validate_update_customer_method():
    try:
        customer_service.update_customer_by_id('10', customer_update)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"


def test_validate_get_customer_method():
    try:
        customer_service.get_customer_by_id('10')
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This customer was not found"


def test_validate_delete_account_method():
    try:
        customer_service.delete_account_by_id('1', 10)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"


def test_validate_delete_customer_method():
    try:
        customer_service.delete_customer_by_id('10')
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"
