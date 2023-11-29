import sqlite3
from os import path, getcwd



class CreateDataBase():
    __sql_create:str = "CREATE TABLE IF NOT EXISTS '{}' ({})"
    __sql_insert:str = "INSERT INTO '{}' VALUES {}"
    __sql_update:str = "UPDATE {} SET {} = '{}' WHERE {}"
    __sql_select:str = "SELECT {columns_name} FROM {table_name} where {check_column_name} = {check_column_value}"
    _db_path:str
    def __init__(self, db_name: str, table_name: str, **kwargs: str) -> None:
        _path: str = getcwd()
        self._db_path :str= path.join(_path, f"{db_name}.db")
        self.name = db_name
        self.table = table_name

        # Add primary keys if exist in kwargs
        self.pri = [f"{p}" for p in kwargs.pop('primary').split(',')] if kwargs.get('primary', '') else ''
        self.primary = f'PRIMARY KEY ("{'","'.join(self.pri)}")' if self.pri else ''

        self.cols = [f"{k} {v.upper()}," for k , v in kwargs.items()]
        self.cols = ''.join(self.cols).strip(',')
        self.columns = self.cols+','+self.primary
        self.create()
    
    def open_db(func):
        def wrapper(*args, **kwargs):
            sql, dbpath = func(*args, **kwargs)
            print(sql,'\n',dbpath)
            try:
                with sqlite3.connect(dbpath) as db:
                    crsr = db.cursor()
                    crsr.execute(sql)
                    db.commit()
            except sqlite3.OperationalError as e:
                print(f'{e.sqlite_errorname}: {e}')
            else:
                return func(*args, **kwargs)
        return wrapper
    
    @open_db
    def create(self)->str:
        # sql:str = self.__sql_create
        return (self.__sql_create.format(self.table, self.columns), self._db_path)
    
    @open_db
    def add_record(self, *values) ->None:
        # sql:str = self.__sql_insert
        return (self.__sql_insert.format(self.table, values), self._db_path)
    
    @open_db
    def update(self,*, column=None, new_value=None, **kwargs):
        """arguments (kwargs): 
        column = column name to be update
        value = new value of column
        **kwargs = conditional selection comes after 'WHERE' in sql
        ex: column='username', new_value='john', username='jack', id='100'

        Returns:
            str: create string like sql for update 
        """        
        list = [f"{k}='{v}'" for k, v in kwargs.items()] #Converts kwargs to string frmat: 'column_to_check=value_to_check'
        WHERE = ' AND '.join(list)
        return (self.__sql_update.format(self.table, column, new_value, WHERE), self._db_path)
                
    def get_query(self):
        pass

    def del_record(self):
        pass

def db_path(self)->str:
    return self._db_path
# @property
# def sql_create(self):
#     return self.__sql_create
# @property
# def sql_insert(self):
#     return self.__sql_insert
# @property
# def sql_update(self):
#     return self.__sql_update
# @property
# def sql_select(self):
#     return self.__sql_select


a = CreateDataBase('amin', 'users', primary='username', username='text unique', password='text not null')
# a.add_record('hamed', 'sdfds')
# a.add_record('amin', '5448')
a.update(column='username', new_value='ola', username='amanada')