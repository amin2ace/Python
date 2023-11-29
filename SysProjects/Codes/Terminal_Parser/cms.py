import os


class Costumer:
    def __init__(self, cm_id, name, email):
        pass
    
    def __str__(self):
        return


class Invoice(Costumer):
    def __init__(self, time_stamp, cm_id, order):
        pass
    
    def __str__(self):
        pass


def create_costumer_db(cm_id, full_name, email):
    #Create a Datebase With costumer ID
    costumer_db = None
    ###Check if the costumer file exsist or not
    if costumer_db:
        return 
    else:
        with open(costumer_db) as r:
            add_costumer = Costumer(cm_id, full_name, email)
            r.writelines(add_costumer)
        return costumer_db

def add_costumer_order(time, cm_id, order_price, costumer_db):
    create_costumer_db(cm_id, full_name,)
    add_record = Invoice(time, cm_id, order_price)


def delete_costumer(cm_id, db_path):
    report(db_path, cm_id)
    pass

def report(db_path, cm_id):
    with open(db_path) as r:
        pass


def main():
    pass

if __name__=="__main__": main()