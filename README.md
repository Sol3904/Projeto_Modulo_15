Este projeto em Python consiste na criação de uma base de dados sqlite com o uso das operações CRUD:

-CREATE

-READ

-UPDATE

-DELETE

Esta base de dados tem como tema champions do jogo League of Legends, sendo usadas as colunas

-Nome

-Dmg

-Lane

Ao longo das tabelas, sendo usada a coluna

-Id

Para garantir a organização das mesmas


Este projeto está atualmente separado em 2 pastas

-sqlite_db

-src

Sendo sqlite_db a pasta que armazena a base de dados

-epbjc.db

E src a pasta que armazena o código, separado por queries

-create

-read

-update

-delete


Dentro de cada pasta estão 3 ficheiros python diferentes, referentes às 3 tabelas a ser criadas, com o nome correspondente às colunas únicas de cada tabela.


No create, estão os queries

-CREATE TABLE e INSERT INTO


No delete, está o query

-DELETE FROM


No read, está o query

-SELECT FROM


No update, está o query

-UPDATE SET


Dentro do champs_read, existe uma opção que permite que o utilizador escolha entre extrair todos os dados da tabela champs e mostra-los no terminal, ou usar o INNER JOIN para unir a tabela champs e a tabela champs_dmg, extraindo e exibindo todas as colunas de ambas as tabelas.
Apesar disto ser funcional, ao usar o INNER JOIN, a informação será repetida entre cada linha das colunas (repete o nome, o id e o dano).

Ainda estamos à procura de uma solução para este problema, visto que a repetição cria redundancias visiveis pelo utilizador.

Dentro do dmg_read, existe uma opçãoo que permite que o utilizador escolha entre extrair todos os dados da tabela champs_dmg e mostra-los no terminal, ou que o utilizador insira um Id especifico para extrair da tabela.
