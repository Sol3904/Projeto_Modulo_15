#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\sqlite_db')
cursor_dmg = conex.cursor()

#solicita ao utilizador o texto correspondete a linha que vai ser apagada
apagar_nome = input("Diga me o nome da linha a apagar ")


#se o nome inserido pelo utilizador existir, as linhas com o nome serão apagadas
#caso contrario, a mensagem "o nome nao foi encontrado" sera exibida
try:
 cursor_dmg.execute('DELETE FROM champs_dmg WHERE champ_nomenome = ?',(apagar_nome,))
except:
 print("O nome não foi encontrado")



#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()