#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\projeto_modulo_15\\sqlite_db\\sqlite.db')
cursor_dmg = conex.cursor()

#atualizar a coluna champ_nome onde id é 1 
cursor_dmg.execute('''UPDATE champs_dmg SET champ_nome = "Taric" WHERE id = 1''')

#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()