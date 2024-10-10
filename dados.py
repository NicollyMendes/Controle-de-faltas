import sqlite3

# Criando o banco de dados
conexao = sqlite3.connect('dados_judoif.db')

# Criar tabela de Alunos
conexao.execute('''CREATE TABLE Alunos(
                    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    endereco TEXT NOT NULL,
                    turma_id INTEGER,
                    FOREIGN KEY (turma_id) REFERENCES Turmas(id_turma))''')

# Criar tabela de Turmas
conexao.execute('''CREATE TABLE Turmas(
                    id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_turma TEXT NOT NULL)''')

# Criar tabela de Frequencia
conexao.execute('''CREATE TABLE Frequencia(
                    id_frequencia INTEGER PRIMARY KEY AUTOINCREMENT,
                    data DATE NOT NULL,
                    presenca BOOLEAN NOT NULL,
                    aluno_id INTEGER,
                    turma_id INTEGER,
                    FOREIGN KEY (aluno_id) REFERENCES Alunos(id_aluno),
                    FOREIGN KEY (turma_id) REFERENCES Turmas(id_turma))''')

# Salvando as alterações e fechando a conexão
conexao.commit()
conexao.close()
