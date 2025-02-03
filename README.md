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

Deverá ser adicionado o inner join assim que possivel
