from data_access_layer.implementation_classes.customer_postgres_dao_imp import CustomerPostgresDAO
from entities.customers import Customer

customer_dao = CustomerPostgresDAO
customer: Customer = Customer(0, "Rey", "Skywalker", "ninja_cat_girl")

update_customer = Customer(0, "Luke", "Skywalker", "master jedi")

delete_customer = Customer(0, "Anakin", "Skywalker", "Cancel Me")


def test_create_customer_entry():
    created_customer = customer_dao.create_customer_entry(customer)
    assert created_customer.customer_id != 0


def test_get_customer_balance_by_id():
    pass


def test_deposit_into_account_by_id():
    pass


def test_withdraw_from_account_by_id():
    pass


def test_transfer_money_by_their_ids():
    pass


def test_update_customer_by_id():
    pass


def test_get_customer_by_id():
    pass


def test_delete_account_by_id():
    pass


def test_delete_customer_by_id():
    pass
