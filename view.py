import sqlite3

# Função criada para conexão com o banco
def connect():
    conexao = sqlite3.connect('dados_judoif.db')
    return conexao

# Função para inserir um novo aluno na tabela Alunos
def insert_student(nome, cpf, telefone, endereco):
    conexao = connect()
    conexao.execute('INSERT INTO Alunos(nome, cpf, telefone, endereco)\
                    VALUES (?, ?, ?, ?)', (nome, cpf, telefone, endereco))
    conexao.commit()
    conexao.close()

# Função para exibir os alunos
def get_students():
    conexao = connect()
    c = conexao.cursor()
    c.execute('SELECT id_aluno, nome, cpf, telefone, endereco, turma_id FROM Alunos')
    alunos = c.fetchall()
    conexao.close()
    return alunos

# Função para buscar os nomes dos alunos
def get_student_names():
    conexao = connect()
    c = conexao.cursor()
    c.execute("SELECT nome FROM Alunos")  # Corrigido para Alunos
    nomes = c.fetchall()
    conexao.close()
    return [nome[0] for nome in nomes]  # Retorna apenas os nomes

# Função para inserir Turma na Tabela Turmas
def insert_class(nome_turma):
    conexao = connect()
    conexao.execute('INSERT INTO Turmas(nome_turma)\
                    VALUES (?)', (nome_turma,))
    conexao.commit()
    conexao.close()

# Função para exibir turmas 
def get_class():
    conexao = connect()
    c = conexao.cursor()
    c.execute('SELECT id_turma, nome_turma FROM Turmas')
    turma = c.fetchall()
    conexao.close()
    return turma

# Função para registrar a falta de um aluno específico, de uma turma específica, em uma data
def insert_absence(aluno_id, id_turma, data, presenca):
    conexao = connect()
    conexao.execute('INSERT INTO Frequencia(aluno_id, turma_id, data, presenca)\
                    VALUES (?, ?, ?, ?)', (aluno_id, id_turma, data, presenca))
    conexao.commit()
    conexao.close()

# Função para exibir as faltas de um aluno
def get_absences_by_student(aluno_id):
    conexao = connect()
    c = conexao.cursor()  # Corrigido o cursor
    # Consulta que faz um JOIN entre Alunos e Frequencia para trazer o nome do Aluno
    c.execute('SELECT A.nome, F.data, F.turma_id, F.presenca\
              FROM Frequencia F\
              JOIN Alunos A ON F.aluno_id = A.id_aluno\
              WHERE A.id_aluno = ?', (aluno_id,))
    faltas = c.fetchall()
    conexao.close()
    return faltas
