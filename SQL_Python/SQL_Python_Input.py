import sqlite3

conexao = sqlite3.connect('Meu_banco_de_dados.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cidade TEXT NOT NULL
    )
''')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite sua cidade: ')

cursor.execute('''
    INSERT INTO pessoas(nome, idade, cidade)
    VALUES (?,?,?)
''', (nome, idade,cidade))

conexao.commit()
cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

for pessoas in pessoas:
    print(f'ID: {pessoas [0]}, Nome: {pessoas [1]}, Idade: {pessoas [2]}, Cidade: {pessoas [3]}')
conexao.close()