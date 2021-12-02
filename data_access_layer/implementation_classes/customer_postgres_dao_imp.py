from data_access_layer.abstract_classes.customer_dao import CustomerDao
from util.database_connection import connection
from entities.customers import Customer


class CustomerPostgresDAO(CustomerDao):
    def create_customer_entry(self, customer: Customer) -> Customer:
        sql = "insert into customer values(default, %s, %s, %s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.customer_id))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        return customer

    def get_customer_balance_by_id(self, customer_id: int, account_id: int) -> float:
        pass

    def deposit_into_account_by_id(self, customer_id: int, account_id: int, amount: int) -> float:
        pass

    def withdraw_from_account_by_id(self, customer_id: int, account_id: int, amount: int) -> float:
        pass

    def transfer_money_by_their_ids(self, customer_id: int, from_account_id: int, to_account_id: int, amount: int) -> \
            float:
        pass

    def update_customer_by_id(self, customer_id: int, customer: Customer) -> Customer:
        sql = 'update customer set first_name = %s, last_name = %s, user_name = %s where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.user_name, customer.customer_id))
        connection.commit()
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        sql = 'select * from customer where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def delete_account_by_id(self, customer_id: int, account_id: int) -> bool:
        sql = 'delete from account where account_id = %s and customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (account_id, customer_id))
        connection.commit()
        return True

    def delete_customer_by_id(self, customer_id: int) -> bool:
        sql = 'delete from customer where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True
