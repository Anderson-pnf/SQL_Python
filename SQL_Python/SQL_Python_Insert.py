import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

con = sqlite3.connect('cliente.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
    )
''')

cursor.execute('''
    INSERT INTO clientes(nome, idade, cidade)
        VALUES('Carla', '25', 'Guarulhos')       
''')
cursor.execute('''
    INSERT INTO clientes(nome, idade, cidade)
        VALUES('Anderson', '24', 'Guarulhos')
''')
cursor.execute('''
    INSERT INTO clientes(nome, idade, cidade)
        VALUES('Amanda','30', 'Guarulhos')
''')
cursor.execute('''
    INSERT INTO clientes(nome, idade, cidade)
        VALUES('Giovanna','20', 'Guarulhos')
''')
cursor.execute('''
    INSERT INTO clientes(nome, idade, cidade)
        VALUES('Matheus','30', 'Guarulhos')
''')       
cursor.execute('''
    INSERT INTO clientes(nome, idade, cidade)
        VALUES('José','50', 'Guarulhos')
''')

con.commit()

df = pd.read_sql_query('SELECT * FROM clientes WHERE idade >= 30', con)
print(df)

cidade_count = df['cidade'].value_counts()
print('contagem', cidade_count)

plt.figure(figsize=(10,6))
cidade_count.plot(kind='bar', color='black')
plt.title('Numero de clientes por cidade')
plt.xlabel('Cidade')
plt.ylabel('Numero de clientes')
plt.xticks(rotation = 45)
plt.show()

con.close()

