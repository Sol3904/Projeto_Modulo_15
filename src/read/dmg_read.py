#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('..\\..\\sqlite_db\\sqlite.db')
cursor_dmg = conex.cursor()

#escolha do utilizador
pergunta = input("Deseja selecionar um id especifico para o SELECT(1) ou quer fazer o SELECT de toda a tabela?(2)")
if(pergunta == "1"):
    try:
         #guarda o id inserido pelo utilizador
         id_util = int(input("Selecione o id a ser extraido:"))

         #extrai os dados da tabela referentes ao id inserido pelo utilizador
         cursor_dmg.execute('SELECT * FROM champs_dmg WHERE id = ?',(id_util,))
         resultados = cursor_dmg.fetchall()
         
         #se não houver resultados
         if not resultados:
             raise ValueError("O ID inserido não existe.")    
    except ValueError as erro:
        print(erro)
elif(pergunta == "2"):
    #extrai todos as colunas da tabela champs_dmg
    cursor_dmg.execute('SELECT * FROM champs_dmg')
    resultados = cursor_dmg.fetchall()
else:
    print("Opção inválida.")

#imprime todos os resultados 
for dmg in resultados:
    print(dmg)

#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()
