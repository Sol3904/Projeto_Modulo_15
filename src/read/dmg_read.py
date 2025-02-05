#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\sqlite_db\\sqlite.db')
cursor_dmg = conex.cursor()

#extrai todos os dados da coluna nomes onde o id é 1
cursor_dmg.execute('SELECT champ_nome FROM champs_dmg WHERE id = 1')

#extrair todas as colunas de champs_dmg
#cursor_dmg.execute('SELECT * FROM champs_dmg')

resultados = cursor_dmg.fetchall()

#imprime todos os resultados 
for dmg in resultados:
    print(dmg)

#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()