#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('..\\..\\sqlite_db\\sqlite.db')
cursor_lanes = conex.cursor()

#extrai todas as colunas da tabela champs_lanes
cursor_lanes.execute('SELECT * FROM champs_lanes')
resultados = cursor_lanes.fetchall()

#imprime todas as colunas com o ciclo for 
for lane in resultados:
    print(lane)

#confirmar alteracoes
conex.commit()
#encerrar a conexao
conex.close()
