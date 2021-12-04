from data_access_layer.abstract_classes.customer_dao import CustomerDao
from util.database_connection import connection
from entities.customers import Customer
from typing import List


class CustomerPostgresDAO(CustomerDao):
    def create_customer_entry(self, customer: Customer) -> Customer:
        sql = 'insert into "python-banking-app".customer values(default, %s, %s, %s) returning customer_id'
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.user_name))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        sql = 'select * from "python-banking-app".customer where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
<<<<<<< HEAD
        customer_record = cursor.fetchone()[0]
=======
        customer_record = cursor.fetchone()
>>>>>>> 9e2631e8804e04f8d77047f4a4b0ad108b61bc58
        customer = Customer(*customer_record)
        return customer

    def get_all_customers(self) -> List[Customer]:
        sql = 'select * from "python-banking-app".customer order by customer_id'
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customers = []
        for customer in customer_records:
            customers.append(Customer(*customer))
        return customers

    def get_customer_balance_by_id(self, customer_id: int, account_id: int) -> float:
        sql = 'select amount from "python-banking-app".account where account_id = %s and customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (account_id, customer_id))
        customer_record = cursor.fetchone()
        return customer_record

    def deposit_into_account_by_id(self, customer_id: int, account_id: int, deposit: float) -> float:
        sql = 'update "python-banking-app".account set amount = %s + amount where account_id = %s ' \
              'and customer_id = %s returning amount'
        cursor = connection.cursor()
        cursor.execute(sql, (deposit, account_id, customer_id))
        connection.commit()
        customer_record = cursor.fetchone()
        return customer_record

    def withdraw_from_account_by_id(self, customer_id: int, account_id: int, withdraw: float) -> float:
        sql = 'update "python-banking-app".account set amount = amount - %s where account_id = %s and customer_id = %s ' \
              'returning amount'
        cursor = connection.cursor()
        cursor.execute(sql, (withdraw, account_id, customer_id))
        connection.commit()
        customer_record = cursor.fetchone()
        return customer_record

    def transfer_money_by_their_ids(self, customer_id: int, from_account_id: int, to_account_id: int,
                                    transfer_amount: float) -> float:
        self.withdraw_from_account_by_id(customer_id, from_account_id, transfer_amount)
        self.deposit_into_account_by_id(customer_id, to_account_id, transfer_amount)
        sql = 'update "python-banking-app".account set amount = %s + amount where account_id = %s and ' \
              'customer_id = %s returning amount'
        cursor = connection.cursor()
        cursor.execute(sql, (transfer_amount, to_account_id, customer_id))
        connection.commit()
        customer_record = cursor.fetchone()
        return customer_record

    def update_customer_by_id(self, customer_id: int, customer: Customer) -> Customer:
        sql = 'update "python-banking-app".customer set first_name = %s, last_name = %s, user_name = %s ' \
              'where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.user_name, customer.customer_id))
        connection.commit()
        return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:
        sql = 'delete from "python-banking-app".customer where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True

