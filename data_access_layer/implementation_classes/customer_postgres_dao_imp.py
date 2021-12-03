from data_access_layer.abstract_classes.customer_dao import CustomerDao
from util.database_connection import connection
from entities.customers import Customer
from typing import List


class CustomerPostgresDAO(CustomerDao):
    def create_customer_entry(self, customer: Customer) -> Customer:
        sql = "insert into customer values(default, %s, %s, %s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.customer_id))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        sql = 'select * from customer where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def get_all_customers(self) -> List[Customer]:
        sql = 'select customer.customer_id, customer.first_name, customer.last_name, customer.last_name, ' \
              'account.account_id, account.account_type, account.amount from customer inner join account ' \
              'on account.customer_id = customer.customer_id order by account.account_id'
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customers = []
        for customer in customer_records:
            customers.append(Customer(*customer))
        return customers

    def get_customer_balance_by_id(self, customer_id: int, account_id: int) -> float:
        sql = 'select amount from account where account_id = %s and customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (account_id, customer_id))
        customer_record = cursor.fetchone()
        return customer_record

    def deposit_into_account_by_id(self, customer_id: int, account_id: int, amount: int) -> float:
        new_balance = self.get_customer_balance_by_id(customer_id, account_id) + amount
        sql = 'update account set amount = %s where account_id = %s and customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (new_balance, account_id, customer_id))
        connection.commit()
        return new_balance

    def withdraw_from_account_by_id(self, customer_id: int, account_id: int, amount: int) -> float:
        new_balance = self.get_customer_balance_by_id(customer_id, account_id) - amount
        sql = 'update account set amount = %s where account_id = %s and customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (new_balance, account_id, customer_id))
        connection.commit()
        return new_balance

    def transfer_money_by_their_ids(self, customer_id: int, from_account_id: int, to_account_id: int, amount: int) -> \
            float:
        self.withdraw_from_account_by_id(customer_id, from_account_id, amount)
        self.deposit_into_account_by_id(customer_id, to_account_id, amount)
        new_balance = self.get_customer_balance_by_id(customer_id, to_account_id)
        sql = 'update account set amount = %s where account_id = %s and customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (new_balance, to_account_id, customer_id))
        connection.commit()
        return new_balance

    def update_customer_by_id(self, customer_id: int, customer: Customer) -> Customer:
        sql = 'update customer set first_name = %s, last_name = %s, user_name = %s where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.user_name, customer.customer_id))
        connection.commit()
        return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:
        sql = 'delete from customer where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True
