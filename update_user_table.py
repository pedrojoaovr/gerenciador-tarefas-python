import sqlite3

# Caminho para o seu banco de dados SQLite
database_path = 'instance/task.db'

# Conecte-se ao banco de dados
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Adicione a coluna 'user_id' à tabela 'task'
cursor.execute('ALTER TABLE task ADD COLUMN user_id INTEGER NOT NULL DEFAULT 1')

# Confirme a alteração
conn.commit()

# Feche a conexão
conn.close()

print("Tabela 'task' atualizada com sucesso.")
