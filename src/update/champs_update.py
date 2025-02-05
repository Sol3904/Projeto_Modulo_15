#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao 
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\projeto_modulo_15\\sqlite_db\\sqlite.db')
cursor = conex.cursor()

#atualiza a coluna nome onde o id é um
cursor.execute('''UPDATE champs SET nome = "Taric" WHERE id = 1''')

#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()