from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException
from data_access_layer.implementation_classes.customer_postgres_dao_imp import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.implementation_services.customer_postgres_service_imp import CustomerPostgresServiceImp

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresServiceImp(customer_dao)

duplicate_customer = Customer(0, "Luke", "Skywalker", "Master Luke")
customer_update = Customer(0, "Luke", "Skywalker", "master jedi")


def test_validate_create_customer_entry():
    try:
        customer_service.service_create_customer_entry(duplicate_customer)
        assert False
    except DuplicateCustomerException as e:
        assert str(e) == "That account has already been created"


def test_validate_get_customer_by_id_method():
    try:
        customer_service.service_get_customer_by_id(10)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This customer was not found"


def test_no_results_for_get_all_customers():
    try:
        customer_service.service_get_all_customers()
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "These accounts were not found"


def test_validate_get_balance_by_id_method():
    try:
        customer_service.service_get_customer_balance_by_id(1, 4)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"


def test_validate_deposit_method():
    try:
        customer_service.service_deposit_into_account_by_id(1, 1, -100)
        assert False
    except InvalidTransactionException as e:
        assert str(e) == "This is not a valid transaction"


def test_validate_withdraw_method():
    try:
        customer_service.service_withdraw_from_account_by_id(1, 1, 2000)
        assert False
    except InvalidTransactionException as e:
        assert str(e) == "This is not a valid transaction"


def test_validate_transfer_method():
    try:
        customer_service.service_transfer_money_by_their_ids(1, 2, 1, 2000)
        assert False
    except InvalidTransactionException as e:
        assert str(e) == "This is not a valid transaction"


def test_validate_update_customer_method():
    try:
        customer_service.service_update_customer_by_id(10, customer_update)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"


def test_validate_delete_customer_method():
    try:
        customer_service.service_delete_customer_by_id(10)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"
