#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao a db
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\projeto_modulo_15\\sqlite_db\\sqlite.db')
cursor_dmg = conex.cursor()

#criar tabela champs_dmg
cursor_dmg.execute('''
CREATE TABLE IF NOT EXISTS champs_dmg (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    champ_nome TEXT NOT NULL,
    dmg TEXT NOT NULL,
    FOREIGN KEY (champ_nome) REFERENCES champs (nome)
)
''')

#inserir dados na tabela champs_dmg
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Teemo","Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Aurelion", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Kindred", "Ad")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Jhin", "Ad")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Braum", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Rell", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Seraphine", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Sona", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("LeBlanc", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Swain", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Sylas", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Ambessa", "Ad")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Aurora", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Smolder", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Singed", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Gnar", "Ad")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Darius", "Ad")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Mordekaiser", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Mordekaiser", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Mordekaiser", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Rakan", "Ap")')
cursor_dmg.execute('INSERT INTO champs_dmg (champ_nome, dmg) VALUES ("Xayah", "Ad")')


#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()