from data_access_layer.implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.customers import Customer

customer_dao_imp = CustomerDaoImp()
customer = Customer("Luke", "Skywalker", "Master Jedi", 1,
                    {"1": {"type": "checking", "balance": 100},
                     "2": {"type": "saving", "balance": 1000}})


def test_create_customer_entry_success():
    new_customer: Customer = customer_dao_imp.create_customer_entry(customer)
    assert new_customer.customer_id != 0

def get_customer_balance_by_id_success():
    returned_customer: Customer = customer_dao_imp.get_customer_balance_by_id(1)
    assert returned_customer.accounts


