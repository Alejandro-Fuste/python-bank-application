from flask import Flask, request, jsonify

from custom_exceptions.duplicate_customer_exception import DuplicateCustomerException
from custom_exceptions.customer_not_found_exception import CustomerNotFoundException
from custom_exceptions.invalid_transaction_exception import InvalidTransactionException

from data_access_layer.implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.customers import Customer
from service_layer.implementation_services.customer_service_imp import CustomerServiceImp

app: Flask = Flask(__name__)

customer_dao = CustomerDaoImp()
customer_service = CustomerServiceImp(customer_dao)


# create customer route
@app.post("/customer")
def create_customer_entry():
    pass


# get customer route
@app.get("/customer/<customer_id>")
def get_customer_information():
    pass


# get all customers route
@app.get("/customers")
def get_all_customers_information():
    pass


# update customer information
@app.patch("/customer/<customer_id>")
def update_customer_information():
    pass


# delete customer information
@app.delete("/customer/<customer_id>")
def delete_customer_information():
    pass


app.run()
