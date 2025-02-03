#importar a biblioteca sqlite3
import sqlite3

#estabelecer a conexao com a base de dados
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\sqlite_db')
cursor = conex.cursor()

#criar tabela champs
cursor.execute('''
CREATE TABLE IF NOT EXISTS champs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

#inserir registos na tabela champs
cursor.execute('INSERT INTO champs (nome) VALUES ("Teemo")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Aurelion")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Kindred")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Jhin")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Braum")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Rell")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Seraphine")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Sona")')
cursor.execute('INSERT INTO champs (nome) VALUES ("LeBlanc")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Swain")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Sylas")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Ambessa")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Aurora")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Smolder")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Singed")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Gnar")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Darius")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Mordekaiser")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Caitlyn")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Vi")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Jinx")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Warwick")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Rammus")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Briar")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Neeko")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Shyvana")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Ornn")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Volibear")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Anivia")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Lissandra")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Olaf")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Gragas")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Tryndamere")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Ashe")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Vayne")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Garen")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Lux")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Galio")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Zoe")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Akali")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Katarina")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Cassiopeia")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Sion")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Jarvan")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Rengar")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Ahri")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Sett")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Rakan")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Xayah")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Soraka")')
cursor.execute('INSERT INTO champs (nome) VALUES ("Yuumi")')


#confirmar alteracoes
conex.commit()
#fechar conexao
conex.close()