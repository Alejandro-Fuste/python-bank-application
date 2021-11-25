from data_access_layer.implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.customers import Customer

customer_dao_imp = CustomerDaoImp()
customer = Customer("Luke", "Skywalker", "Master Jedi", 1,
                    {"1": {"type": "checking", "balance": 100},
                     "2": {"type": "saving", "balance": 1000}})
updated_info = Customer("Luke", "Skywalker", "Master Luke", 1,
                       {"1": {"type": "checking", "balance": 100},
                        "2": {"type": "saving", "balance": 1000}})


def test_create_customer_entry_success():
    new_customer: Customer = customer_dao_imp.create_customer_entry(customer)
    assert new_customer.customer_id != 0


def get_customer_balance_by_id_success():
    returned_customer: Customer = customer_dao_imp.get_customer_balance_by_id(1)
    assert returned_customer != 0


def deposit_into_account_by_id_success():
    pass


def withdraw_from_account_by_id_success():
    pass


def transfer_money_between_accounts_by_their_ids_success():
    pass


def update_customer_by_id_success():
    updated_customer: Customer = customer_dao_imp.update_customer_by_id(updated_info)
    assert updated_customer.user_name == updated_info.user_name


def get_customer_by_id_success():
    selected_customer = customer_dao_imp.get_customer_by_id(1)
    assert selected_customer.customer_id == 1


def delete_account_by_id_success():
    selected_account = customer_dao_imp.delete_account_by_id(6)
    assert selected_account


def delete_customer_by_id_success():
    selected_customer = customer_dao_imp.delete_customer_by_id(3)
    assert selected_customer
