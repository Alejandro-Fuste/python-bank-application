from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException
from data_access_layer.implementation_classes.account_postgres_dao_imp import AccountPostgresDAO
from entities.accounts import Account
from service_layer.implementation_services.account_postgres_service_imp import AccountPostgresServiceImp

account_dao = AccountPostgresDAO()
account_service = AccountPostgresServiceImp(account_dao)

duplicate_account = Account(0, 'checking', 100.00, 1)


def test_duplicate_account_for_create_account():
    try:
        account_service.create_account(duplicate_account)
        assert False
    except DuplicateCustomerException as e:
        assert str(e) == "That account has already been created"


def test_no_results_for_get_all_customers():
    try:
        account_service.get_all_customers()
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "These accounts were not found"


def test_no_results_for_get_all_accounts():
    try:
        account_service.get_all_accounts()
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "These accounts were not found"


def test_not_found_for_get_all_customer_accounts_by_id():
    try:
        account_service.get_all_customer_accounts_by_id()
        assert False
    except CustomerNotFoundException as e:
        assert str(e) == "These accounts were not found"
