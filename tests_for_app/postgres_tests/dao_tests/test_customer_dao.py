from data_access_layer.implementation_classes.customer_postgres_dao_imp import CustomerPostgresDAO
from entities.customers import Customer

customer_dao = CustomerPostgresDAO()
customer: Customer = Customer(0, "Rey", "Skywalker", "ninja_cat_girl")

update_customer = Customer(0, "Luke", "Skywalker", "master jedi")

delete_customer = Customer(0, "Anakin", "Skywalker", "Cancel Me")


def test_create_customer_entry_success():
    created_customer = customer_dao.create_customer_entry(customer)
    assert created_customer.customer_id != 0


def test_get_customer_balance_by_id_success():
    customer_balance = customer_dao.get_customer_balance_by_id(1, 1)
    assert customer_balance != 0


def test_deposit_into_account_by_id_success():
    original_balance = customer_dao.get_customer_balance_by_id(1, 1)
    new_balance = customer_dao.deposit_into_account_by_id(1, 1, 100)
    assert new_balance > original_balance


def test_withdraw_from_account_by_id_success():
    customer_balance = customer_dao.get_customer_balance_by_id()
    assert


def test_transfer_money_by_their_ids_success():
    customer_balance = customer_dao.get_customer_balance_by_id()
    assert


def test_update_customer_by_id_success():
    customer_balance = customer_dao.get_customer_balance_by_id()
    assert


def test_get_customer_by_id_success():
    customer_balance = customer_dao.get_customer_balance_by_id()
    assert


def test_delete_account_by_id_success():
    customer_balance = customer_dao.get_customer_balance_by_id()
    assert


def test_delete_customer_by_id_success():
    customer_balance = customer_dao.get_customer_balance_by_id()
    assert
