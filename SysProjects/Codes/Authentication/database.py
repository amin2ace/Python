import logging
import os
import sqlite3
from typing import Self


class CreateDB:
    """dec: CREATE table with name of db_name, in self.db path
    colmns pass as key word args witch keys are column names and values are column data type
    primary_key keyarg act as primary key column in table with is one of the column names
    ex: database = CreateDB('table', 'std_id', std_id='INTEGER', name='TEXT')
    class is logging enabled"""

    def __init__(self, table_name: str, primary_key: str = "", **args) -> None:
        self.db: str
        log_file, x = os.path.split(self.db)
        log_file = os.path.join(log_file, "loger.log")
        logging.basicConfig(
            filename=log_file, format="%(asctime)s %(message)s", filemode="a"
        )
        self.log = logging.getLogger()
        self.log.setLevel(10)

        self.table: str = table_name
        self.columns: str = ""
        self.args = args
        self.primary = primary_key

        for col, datatype in args.items():
            self.columns += f"'{col}' {datatype.upper()},"  # Add columns to string type query witch givin by key args -> str

        if self.primary:
            self.columns += f"PRIMARY KEY ('{self.primary}') "  # Add primary key to string type query if givin -> str

        self.sql = self.columns[
            0 : len(self.columns) - 1
        ]  # Make query for create table
        try:
            assert self.primary in self.args.keys()
        except:
            self.log.error("Primary key must be one of the columns")
        else:
            with sqlite3.connect(self.db) as db:
                try:
                    # log an Info level log if table created successfully
                    # log a Debug level log if table exists
                    db.cursor().execute(f"CREATE TABLE {self.table} ({self.sql})")
                    db.commit()
                    self.log.info(
                        f" Table '{self.table}' successfully created in '{self.db}'"
                    )
                except:
                    self.log.debug(f" Table '{self.table}' Detected")

    @classmethod
    def db_path(cls, database_path: str):
        """Defines database path to be created in string.

        to create in current working directory enter file
        name only.

        filename extension must be " .db "

        ex:  C:/New_Folder/database.db"""

        path_, file = os.path.split(database_path)
        path_ = os.path.join(os.getcwd(), path_)
        if os.path.isdir(path_):
            cls.db = os.path.join(path_, file)
            # return logging.debug(" Data base diractory detected.")
        else:
            os.mkdir(path_)
            cls.db = os.path.join(path_, file)
            # return logging.debug(" Data base directory established.")

    def add_record(self, *data) -> None:
        """1. Gives Error level log if records not match columns
        2. Gives Error level log if primary key not uniqe
        3. Gives Info level log if record added successfully"""
        try:
            assert len(data) == len(self.args)
        except:
            return self.log.error(" Records numbers didn't match column numbers")
        else:
            with sqlite3.connect(self.db) as db:
                try:
                    db.cursor().execute(f"INSERT INTO {self.table} VALUES {data}")
                    db.commit()
                    self.log.info(f" Record Successfully added: {data[0]}")
                except:
                    self.log.error(
                        f" Primary key must have Unique Value: '{self.table}.{self.primary}'"
                    )

    def check(self, table: str, **args: str) -> tuple:
        """1. Returns record in a tuple if exists
        2. Returns empty tuple and Debug level log if not exists
        """
        sql: str = ""
        for col, value in args.items():
            sql += f"{col}='{value}' AND "
        sql = sql[0 : len(sql) - 4]
        # print(sql)
        with sqlite3.connect(self.db) as db:
            try:
                query = db.cursor().execute(f"SELECT * FROM {table} WHERE {sql}")
                return query.fetchall()[0]
            except:
                self.log.debug(f"Record {args} not exist")
                return tuple()


class PrimaryKey(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Primary key must have Unique Value:")
