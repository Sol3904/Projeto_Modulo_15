#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('..\\..\\sqlite_db\\sqlite.db')
cursor = conex.cursor()

pergunta = input("Quer ler a união entre a tabela do dano e dos champions(1), ou apenas a do champions(2)?")
if pergunta == "1":
    #extrair todas as colunas da tabela champs e da tabela champs_dmg, e une as colunas onde os nomes coincidem
    cursor.execute('SELECT DISTINCT * FROM champs INNER JOIN champs_dmg ON champs.nome = champs_dmg.champ_nome')
    resultados = cursor.fetchall()
elif pergunta == "2":
    #extrair todas as colunas da tabela champs
    cursor.execute('SELECT * FROM champs')
    resultados = cursor.fetchall()
else:
    #caso a opcao inserida pelo utilizador nao exista
    print("Opção inválida")

#imprime todas as colunas, uma a uma, com o ciclo for 
for champ in resultados:
    print(champ)

#confirmar alteracoes
conex.commit()
#encerrar conexoes
conex.close()
