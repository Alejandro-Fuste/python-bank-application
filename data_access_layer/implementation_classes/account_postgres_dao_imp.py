from typing import List

from data_access_layer.abstract_classes.account_dao import AccountDao
from entities.accounts import Account
from util.database_connection import connection


class AccountPostgresDAO(AccountDao):

    def create_account(self, account: Account) -> Account:
        sql = 'insert into "python-banking-app".account values(default, %s, %s, %s) returning account_id'
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_type, account.amount, account.customer_id))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        account.account_id = generated_id
        return account

    def get_all_accounts(self) -> List[Account]:
        sql = 'select * from "python-banking-app".account order by account_id'
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        accounts = []
        for account in account_records:
            accounts.append(Account(*account))
        return accounts

    def get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        sql = 'select * from "python-banking-app".account where customer_id = 1 order by account_id'
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        accounts = []
        for account in account_records:
            accounts.append(Account(*account))
        return accounts

    def delete_account_by_id(self, customer_id: int, account_id: int) -> bool:
        sql = 'delete from "python-banking-app".account where account_id = %s and customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (account_id, customer_id))
        connection.commit()
        return True
