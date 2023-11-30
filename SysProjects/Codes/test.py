
# t = {'name':'amin', 'age':25}
# g = {'name':'amin', 'we':70}

# print({**t, **g})

def one():
    print(f'one')

def two():
    print(f'two')

def three():
    print(f'Three')
var = 1
dic = {1:one, 2:two, 3:three}

final = dic.get(var)
final()