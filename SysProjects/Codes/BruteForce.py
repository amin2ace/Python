import csv
import json

class Guess:
    def __init__(self, phrase: str | int) -> None:
        self.phrase: str | int = phrase

    def get_number(self):
        if not isinstance(self.phrase, int):
            return 0
        g_number = 0
        import timeit

        t_1: float = timeit.default_timer()
        while g_number != self.phrase:
            g_number += 1
        else:
            t_2: float = timeit.default_timer()
            return f"Number is: {g_number}\tin {(t_2-t_1)} s"

    def get_phrase(self, depth: int = 2, include_digit: bool = False):
        import random as r
        import timeit

        resource_list: list = [chr(l) for l in range(97, 123)]
        if include_digit:
            resource_list.extend([n for n in range(0, 10)])
        phrase: str = ""
        t_1: float = timeit.default_timer()
        while phrase != self.phrase:
            sam_list: list = r.sample(resource_list, depth)
            phrase = "".join(sam_list)

        else:
            t_2: float = timeit.default_timer()
            return f"Phrase Founded: {phrase}\tin {t_2-t_1} s"

    @staticmethod    
    def get_common(commons, database):
        try:
            with open(database, 'a') as db:
                wr = csv.writer(db)
                head:list = ['num', 'pass']
                wr.writerow(head)
                num:int = 0
                with open(commons, 'r') as c:
                    reading: list = c.readlines()
                    for r in reading:
                        read = [num, r.strip()]
                        wr.writerow(read)
                        num +=1
                        print(read)
        except ValueError as e:
            print(f'File Error: {e}')
        else:
            print('Database Updated!')
            return database

    def check_common(self, database):
        com: dict = dict()
        try:
            with open(database, 'r') as db:
                read = db.readline()
                for line in read:
                    print(line)
                    # com[read[0]] = read[1]
        except ValueError as e:
            print(f"Database Not Found: {e}")
        
        else:
            for i, j in com.items():
                if self.phrase == j:
                    return f'{i} : {j}'
                else:
                    print(i, j)

db =Guess.get_common('D:\Python\Projects\Codes\comm.txt', 'Projects\Codes\database.csv')
print(Guess('password').check_common(db))