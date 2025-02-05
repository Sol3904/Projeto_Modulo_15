#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\projeto_modulo_15\\sqlite_db\\sqlite.db')
cursor_lanes = conex.cursor()

#confirmacoes de mau gosto
pergunta = input("Quer apagar a tabela champs_lanes? ")
if pergunta == "sim":
    crtz = input("Tem a certeza? ")
    if crtz == "sim":
        absoluta = input("Tem a certeza absoluta? ")
        if absoluta == "sim":
            warning = input("Cuidado que vai tudo á vida, quer MESMO? ")
            if warning == "sim":
                #apagar a tabela champs_lanes
                cursor_lanes.execute('DELETE FROM champs_lanes')

if pergunta or crtz or absoluta or warning == "nao":
    print("Obrigada meu")


#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()