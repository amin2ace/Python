import sqlite3
dis = {'username':'TEXT', 'password':'TEXT'}
col = ''
for i, j in dis.items():
    col += f'"{i}" {j},'
    
print(col)
# print(columns)
# with sqlite3.connect("data.db") as db:
#     db.cursor().execute(f"CREATE TABLE IF NOT EXISTS user {columns}")

