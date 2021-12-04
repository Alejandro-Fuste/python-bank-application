from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from data_access_layer.implementation_classes.account_postgres_dao_imp import AccountPostgresDAO
from entities.accounts import Account
from service_layer.implementation_services.account_postgres_service_imp import AccountPostgresServiceImp

account_dao = AccountPostgresDAO()
account_service = AccountPostgresServiceImp(account_dao)

duplicate_account = Account(0, 'checking', 100.00, 1)


def test_duplicate_account_for_create_account():
    try:
        account_service.service_create_account(duplicate_account)
        assert False
    except DuplicateCustomerException as e:
        assert str(e) == "That account has already been created"


def test_not_found_for_get_all_customer_accounts_by_id():
    try:
        account_service.service_get_all_customer_accounts_by_id(100)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"


def test_validate_delete_account_method():
    try:
        account_service.service_delete_account_by_id(1, 10)
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "This account was not found"
