#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\sqlite_db')
cursor_lanes = conex.cursor()

#atualiza a coluna lane onde o id é 1
cursor_lanes.execute('''UPDATE champs_lanes SET lane = "Top" WHERE id = 1''')

#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()