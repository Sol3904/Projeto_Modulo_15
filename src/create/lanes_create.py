#importar biblioteca sqlite3
import sqlite3

#estabelecer conexao
conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\projetom15\\projeto_modulo_15\\sqlite_db\\sqlite.db')
cursor_lanes = conex.cursor()

#criar tabela champs_lanes
cursor_lanes.execute('''
CREATE TABLE IF NOT EXISTS champs_lanes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    champ_nome TEXT NOT NULL,
    lane TEXT NOT NULL,
    FOREIGN KEY (champ_nome) REFERENCES champs (nome)
    
)
''')



#inserir dados na tabela champs_lanes
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Teemo", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Aurelion", "Mid")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Kindred", "Jgl")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Jhin", "Adc")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Braum", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Rell", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Seraphine", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Sona", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("LeBlanc", "Mid")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Swain", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Sylas", "Mid")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Ambessa", "Jgl")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Aurora", "Mid")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Smolder", "Adc")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Singed", "Top")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Gnar", "Top")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Darius", "Top")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Mordekaiser", "Top")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Rakan", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (champ_nome, lane) VALUES ("Xayah", "Adc")')


#confirmar alteracoes
conex.commit()
#encerrar conexao
conex.close()