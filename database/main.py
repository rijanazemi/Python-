import sqlite3
from tkinter.tix import INTEGER

connection = sqlite

cursor.execute(
    '''
     INSERT INTO employees (name, position, department, salary)
     values (?'?'?'?)
     ''', ('john', 'software engineer', 'it', 70000.00)
)

connection.commit()

cursor.execute('SELECT * FROM employees')

rows = cursos.fetchall()

for row in rows:
    print(row)


cursos.execute('''
    UPDATE employees SET salary = ?
    WHERE name = ?
''',(80000.00, 'john')

)
connection.commit()

cursor.execute( '''
    DELETE FROM employees WHERE id = ?
    
''', (1,)
)

connection.commit()
cursor.close()
connection.close()
