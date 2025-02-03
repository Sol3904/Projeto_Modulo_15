#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\sqlite_db')
cursor = conex.cursor()

#confirmacoes de mau gosto
pergunta = input("Quer apagar a tabela champs? ")
if pergunta == "sim":
    crtz = input("Tem a certeza? ")
    if crtz == "sim":
        absoluta = input("Tem a certeza absoluta? ")
        if absoluta == "sim":
            warning = input("Cuidado que vai tudo á vida, quer MESMO? ")
            if warning == "sim":
                #apagar tabela champs
                cursor.execute('DELETE FROM champs')

if pergunta or crtz or absoluta or warning == "nao":
    print("Obrigada meu")

#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()