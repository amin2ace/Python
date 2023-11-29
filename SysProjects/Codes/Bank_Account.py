import sqlite3
import os
from sqlite3 import Cursor
from datetime import datetime as stamp



class Create_DataBase():
    def __init__(self, db_name: str, table_name: str, *columns_name: str) -> None:
        db_path: str = r"C:\Users\Deathkiss\Documents\VS_Code\.venv\ClassBased"
        self.db_path = os.path.join(db_path, f"{db_name}.db")
        self.name = db_name
        self.table = table_name
        self.columns = columns_name
        self.create_db()

    def create_db(self):
        sql_1:str = f"CREATE TABLE IF NOT EXISTS _{self.table} {self.columns}"
        with sqlite3.connect(self.db_path) as self.accounts_db:
            self.curser: Cursor = self.accounts_db.cursor()
            self.curser.execute(sql_1)
            self.accounts_db.commit()

    def add_record(self, *values: str) ->None:
        with sqlite3.connect(self.db_path) as self.accounts_db:
            curser = self.accounts_db.cursor()
            ### Adding Date and Time Stamps to record
            column_values = self.add_time_stamp(values)
            sql_2:str = f"INSERT INTO _{self.table} VALUES {column_values}"
            curser.execute(sql_2)
            self.accounts_db.commit()

    def add_time_stamp(self, values):
        ### Adding Date and Time Stamps to record
        column_values: list = [value for value in values] ### Convert Record To list to be addale
        column_values.insert(0, str(stamp.date(stamp.now())))
        column_values.insert(1, str(stamp.time(stamp.now())))
        return tuple(column_values) ### Convert Back to Tuple
        
    def update_record(self, update_column: str, new_value, check_column_name: str, check_column_value) -> None:
        sql_3:str = f"UPDATE _{self.table} SET {update_column} = {new_value} WHERE {check_column_name} = {check_column_value}"
        with sqlite3.connect(self.db_path) as accounts_db:
            curser = accounts_db.cursor()
            curser.execute(sql_3)

    def get_query(self, check_column_name:str, check_column_value = 0) -> int:
        sql_4 = f"SELECT {check_column_name} FROM _{self.table} where {check_column_name} = {check_column_value}"     
        sql_5 = f"SELECT last_value({check_column_name}) OVER(ORDER by ROWID DESC) from _{self.table} LIMIT 1"  
        with sqlite3.connect(self.db_path) as query:
            cursor = query.cursor()
            if not check_column_value:
                query_ = cursor.execute(sql_5)
                check: list = query_.fetchone()
                return check[0]
            else:
                query_ = cursor.execute(sql_4)
                check: list = query_.fetchone()
                return check


    def del_record(self):
        pass

class BankAccount():

    def __init__(self, bank_name: str, id_number:int, first_name:str, last_name:str, bank_path: str = 0) -> None:
        #self.DB_Directory() = r"C:\Users\Deathkiss\Documents\VS_Code\Bank_DB"
        self.account_id, self.first_name, self.last_name, = id_number, first_name, last_name
        self.bank_name:str = bank_name
        self.bank_path = bank_path
        self.Bank_db = Create_DataBase(self.bank_name, 'Accounts_Table',
                                       'Date_Stamp', 'Time_Stamp', 'ID_Number', 'First_Name', 'Last_Name', 'Balance_$')
        self.account = Create_DataBase(self.bank_name, self.account_id, 'Date_Stamp', 'Time_Stamp', 'Deposit/WithDraw', 'Balance_$')

    def create_account(self, initial_deposit:int = 0):
        ### add bank data base a new record for the account
        query = self.Bank_db.get_query('ID_Number', self.account_id)
        if not query:
            self.balance = 0
            self.balance += initial_deposit
            self.Bank_db.add_record(self.account_id, self.first_name, self.last_name, initial_deposit)
            self.account.add_record(f'+{self.balance}', self.balance)
        return self.account

    ## Deposit amount to account
    def deposit(self, amount:int, wage=0):
        # self.account = self.create_account
        self.balance = self.account.get_query('Balance_$')
        amount -= wage
        self.balance += amount
        self.Bank_db.update_record('Balance_$', self.balance, 'ID_Number', self.account_id)
        self.account.add_record(f'+{amount}', self.balance)

    ## Withdraw amount from account if can withdraw
    def withdraw(self, amount:int, wage=0):
        self.balance = self.can_withdraw(amount)
        if self.balance:
            amount += wage
            self.balance -= amount
            self.account.add_record(f'-{amount}', self.balance)
            self.Bank_db.update_record('Balance_$', self.balance, 'ID_Number', self.account_id)

    def can_withdraw(self, amount:int = 0):
        self.balance = self.account.get_query('Balance_$')
        if self.balance >= amount:
            return self.balance
        return 0

class Accounts(BankAccount):
    def __init__(self, bank_name:str, id_number:int, first_name:str, last_name:str, email:str, initial_deposit:int = 0):
        self.email = email
        super().__init__(bank_name, id_number, first_name, last_name, initial_deposit)

class LowBalance(Exception):
    def __init__(self, message):
        super().__init__(message)

class NoAccount(Exception):
    def __init__(self, message):
        super().__init__(message)


def main():
    amin = Accounts('First_Bank_DB', 1361616441, 'amin', 'vahdani','amin@email.com')
    hamed = Accounts('First_Bank_DB', 1371515661, 'hamed', 'vahdani','hamed@email.com')
    ati = Accounts('First_Bank_DB', 1885151331, 'ati', 'vahdani','ati@email.com')
    # amin.create_account(200)
    # hamed.create_account(500)
    # ati.create_account(1000)
    # amin.deposit(800)
    # hamed.withdraw(500)
    # ati.deposit(2000)
    # amin.deposit(300)
    # hamed.deposit(320)
    # ati.withdraw(600)

if __name__=="__main__":main()

