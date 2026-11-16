import sqlite3 # banco de dados em python
from pathlib import Path # biblioteca para manipular caminhos de arquivos

CAMINHO_BANCO = path = Path(__file__).parent / "banco.db" # caminho do banco de dados 

# Cria tabela clientes
SQL_TABELAS ="""CREATE TABLE IF NOT EXISTS clientes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
cpf TEXT NOT NULL,
data_nascimento TEXT,
telefone TEXT,
email TEXT,
creado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- cria tabela contas
CREATE TABLE IF NOT EXISTS contas(
id INTEGER PRIMARY KEY AUTOINCREMENT,
numero TEXT NOT NULL,
agencia TEXT NOT NULL DEFAULT '0001',
tipo TEXT NOT NULL CHECK(tipo IN ('corrente', 'poupanca')),
saldo_centavos INTEGER NOT NULL DEFAULT 0,
status TEXT NOT NULL DEFAULT 'ativa',
cliente_id INTEGER NOT NULL REFERENCES clientes(id),
criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);

--criar tabela transacoes
CREATE TABLE IF NOT EXISTS transacoes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
conta_id INTEGER NOT NULL REFERENCES contas(id),
tipo TEXT NOT NULL,
valor_centavos INTEGER NOT NULL CHECK (valor_centavos > 0),
saldo_apos_centavos INTEGER NOT NULL,
conta_destino_id INTEGER REFERENCES contas(id),
 criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
 );
"""

# Define a função que abre a conexão com o banco de dados
def conectar():
# abre a conexão com o banco de dados
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row # permite acessar os resultados como dicionários
    conexao.execute("PRAGMA foreign_keys = ON") # habilita o suporte a chaves estrangeiras
    return conexao

# Define a função que cria as tabelas no banco de dados
def criar_tabelas():
    conexao = conectar() # abre a conexão com o banco de dados
    conexao.executescript(SQL_TABELAS) # executa o script SQL para criar as tabelas
    conexao.close() # fecha a conexão com o banco de dados
