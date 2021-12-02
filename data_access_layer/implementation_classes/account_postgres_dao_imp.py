from typing import List

from data_access_layer.abstract_classes.account_dao import AccountDao
from entities.accounts import Account
from entities.customers import Customer
from util.database_connection import connection


class AccountPostgresDAO(AccountDao):

    def create_account(self, account: Account) -> Account:
        sql = 'insert into account values(default, %s, %s, %s) returning account_id'
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_type, account.amount, account.customer_id))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        account.account_id = generated_id
        return account

    def get_all_customers(self) -> List[Customer]:
        sql = 'select * from customer order by customer_id'
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customers = []
        for customer in customer_records:
            customers.append(Customer(*customer))
        return customers

    def get_all_accounts(self) -> List[Account]:
        sql = ''
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        accounts = []
        for account in account_records:
            accounts.append(Account(*account))
        return accounts

    def get_all_customer_accounts_by_id(self, customer_id: int) -> Customer:
        sql = ''
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer
