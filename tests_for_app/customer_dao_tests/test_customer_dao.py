from data_access_layer.implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.customers import Customer

customer_dao_imp = CustomerDaoImp()
customer = Customer("Luke", "Skywalker", "Master Jedi", 1, {"checking": {}})


def test_create_customer_entry():
    pass
