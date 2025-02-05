#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\projeto_modulo_15\\sqlite_db\\sqlite.db')
cursor = conex.cursor()

#extrair todas as colunas da tabela champs
cursor.execute('SELECT DISTINCT * FROM champs INNER JOIN champs_dmg ON champs.nome = champs_dmg.champ_nome GROUP BY champs.nome, champs_dmg.champ_nome ')
resultados = cursor.fetchall()

#imprime todas as colunas, uma a uma, com o ciclo for 
for champ in resultados:
    print(champ)

#confirmar alteracoes
conex.commit()
#encerrar conexoes
conex.close()