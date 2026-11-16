from app.database import conectar,criar_tabelas #importa as funções do arquivo database.py

criar_tabelas()#chama a função criar_tabelas para criar as tabelas no banco de dados

conexao = conectar() #chama a função conectar para abrir a conexão com o banco de dados
tabelas = conexao.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';").fetchall() #executa a consulta para listar as tabelas no banco de dados
conexao.close() #fecha a conexão com o banco de dados

print("Tabelas criadas com sucesso!") #imprime a mensagem de sucesso
for tabela in tabelas: #percorre cada tabela encontrada, uma de cada vez
    print("-", tabela["name"]) #imprime o nome da tabela