from data_access_layer.implementation_classes.account_postgres_dao_imp import AccountPostgresDAO
from entities.accounts import Account

account_dao = AccountPostgresDAO
new_account = Account(0, 'checking', 100.00, 1)


def test_create_account():
    account_result = account_dao.create_account(new_account)
    assert account_result.account_id != 0


def test_get_all_customers():
    pass


def test_get_all_accounts():
    pass


def test_get_all_customer_accounts_by_id():
    pass
