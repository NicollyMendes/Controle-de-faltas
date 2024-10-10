from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import xlsxwriter
# importando as funções da view
from view import *


# Criando janela principal ------ 
janela = Tk()
janela.title('Sistema de Frequência de Alunos')
janela.geometry('800x400')  # Tamanho inicial maior para testar a responsividade
janela.configure(background='#f0f0f5')
janela.resizable(True, True)  # Permitir redimensionamento

# Estilo e layout
style = Style(janela)
style.theme_use('clam')

# Configurar o layout da janela para expandir conforme o tamanho
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=3)
janela.grid_rowconfigure(1, weight=1)

# Frames principais
frameCima = Frame(janela, background='#4CAF50', relief='flat')  # Cor de destaque
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsq = Frame(janela, background='#f0f0f5', relief='solid')
frameEsq.grid(row=1, column=0, sticky=NSEW)

frameDir = Frame(janela, background='#ffffff', relief='raised')  # Fundo branco
frameDir.grid(row=1, column=1, sticky=NSEW)

# Responsividade dos frames
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=3)  # Frame da direita ocupa mais espaço
janela.grid_rowconfigure(1, weight=1)

frameEsq.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
frameEsq.grid_columnconfigure(0, weight=1)

frameDir.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
frameDir.grid_columnconfigure(0, weight=1)
frameDir.grid_columnconfigure(1, weight=3)  # Adiciona peso para expandir melhor as caixas de texto


# Função para cadastro de novos Alunos
def novo_aluno():
    for widget in frameDir.winfo_children():
        widget.destroy()

    def add():
        nome = e_nome.get()
        cpf = e_cpf.get()
        telefone = e_telefone.get()
        endereco = e_endereco.get()

        if nome == '' or cpf == '' or telefone == '' or endereco == '':
            messagebox.showerror('ERRO', 'Preencha todos os campos!')
            return

        insert_student(nome, cpf, telefone, endereco)
        messagebox.showinfo('Sucesso', 'Aluno cadastrado com sucesso!')
        e_nome.delete(0, END)
        e_cpf.delete(0, END)
        e_telefone.delete(0, END)
        e_endereco.delete(0, END)

    # Interface para novo aluno
    Label(frameDir, text='Nome*', anchor=NW, font=('Ivy 10'), bg='#f0f0f5', fg='#333333').grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)
    e_nome = Entry(frameDir, justify='left', relief='solid', bg='#ffffff', fg='#333333')
    e_nome.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    Label(frameDir, text='CPF*', anchor=NW, font=('Ivy 10'), bg='#f0f0f5', fg='#333333').grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_cpf = Entry(frameDir, justify='left', relief='solid', bg='#ffffff', fg='#333333')
    e_cpf.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    Label(frameDir, text='Telefone*', anchor=NW, font=('Ivy 10'), bg='#f0f0f5', fg='#333333').grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_telefone = Entry(frameDir, justify='left', relief='solid', bg='#ffffff', fg='#333333')
    e_telefone.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    Label(frameDir, text='Endereço*', anchor=NW, font=('Ivy 10'), bg='#f0f0f5', fg='#333333').grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_endereco = Entry(frameDir, justify='left', relief='solid', bg='#ffffff', fg='#333333')
    e_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    Button(frameDir, command=add, text='Salvar', bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE, activebackground='#45a049').grid(row=5, column=1, pady=10, sticky=NSEW)


# Função para registrar a presença
def registrar_presenca():
    for widget in frameDir.winfo_children():
        widget.destroy()

    def add_presenca():
        aluno_id = e_id_aluno.get()
        turma_nome = combobox_turmas.get()  # Pega a turma do combobox
        data_atual = date.today().strftime('%Y-%m-%d')

        if turma_nome == "Turma Infantil":
            turma_id = 1
        elif turma_nome == "Turma Adulta":
            turma_id = 2
        else:
            messagebox.showerror('ERRO', 'Selecione uma turma válida!')
            return

        if not aluno_id:
            messagebox.showerror('ERRO', 'Preencha todos os campos!')
            return

        insert_absence(aluno_id, turma_id, data_atual, True)
        messagebox.showinfo('Sucesso', 'Presença registrada com sucesso!')
        e_id_aluno.delete(0, END)

    # Interface gráfica
    Label(frameDir, text='Registrar Presença', width=50, compound=LEFT, padx=5, pady=5, font=('Verdana 12'), bg='#4CAF50', fg='white').grid(row=0, column=0, columnspan=2, sticky=NSEW)

    Label(frameDir, text='ID do Aluno*', anchor=NW, font=('Ivy 10'), bg='#f0f0f5', fg='#333333').grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_aluno = Entry(frameDir, justify='left', relief='solid', bg='#ffffff', fg='#333333')
    e_id_aluno.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    Label(frameDir, text='Turma*', anchor=NW, font=('Ivy 10'), bg='#f0f0f5', fg='#333333').grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    combobox_turmas = Combobox(frameDir, values=["Turma Infantil", "Turma Adulta"], state="readonly")
    combobox_turmas.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    combobox_turmas.current(0)

    Button(frameDir, command=add_presenca, text='Registrar Presença', bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE).grid(row=3, column=1, pady=5, sticky=NSEW)


# Função para exibir alunos
def ver_alunos():
    for widget in frameDir.winfo_children():
        widget.destroy()

    app_ = Label(frameDir, text='Alunos', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#4CAF50', fg='white')
    app_.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    dados = get_students()
    list_header = ['ID', 'Nome', 'CPF', 'Telefone', 'Endereço']

    global tree
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew', columnspan=2)
    vsb.grid(column=2, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew', columnspan=2)

    # Definir largura e comportamento de colunas
    hd = ["nw", "nw", "nw", "nw", "nw"]
    h = [50, 150, 150, 150, 150]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n], stretch=True)
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)


# Função para ver a frequência
def ver_frequencia():
    for widget in frameDir.winfo_children():
        widget.destroy()

    Label(frameDir, text='Frequência dos Alunos', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='lightgray', fg='black').grid(row=0, column=0, columnspan=2, sticky=NSEW)

    Label(frameDir, text='ID do Aluno*', anchor=NW, font=('Ivy 10'), bg='#f0f0f5', fg='#333333').grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_aluno = Entry(frameDir, justify='left', relief='solid', bg='#ffffff', fg='#333333')
    e_id_aluno.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    def buscar_frequencia():
        aluno_id = e_id_aluno.get()
        if not aluno_id:
            messagebox.showerror('Erro', 'Por favor, insira o ID do Aluno')
            return

        dados = get_absences_by_student(aluno_id)
        if not dados:
            messagebox.showinfo('Informação', 'Nenhuma frequência encontrada para este aluno.')
            return

        list_header = ['Nome', 'Data', 'Turma', 'Presença']

        global tree
        tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)
        hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=4, sticky='nsew', columnspan=2)
        vsb.grid(column=2, row=4, sticky='ns')
        hsb.grid(column=0, row=5, sticky='ew', columnspan=2)

        hd = ["nw", "nw", "nw", "nw"]
        h = [50, 150, 150, 150]
        n = 0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            tree.column(col, width=h[n], anchor=hd[n], stretch=True)
            n += 1

        for item in dados:
            tree.insert('', 'end', values=item)

    Button(frameDir, text="Buscar Frequência", command=buscar_frequencia, bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE).grid(row=3, column=1, pady=10, sticky=NSEW)


# Função para gerar relatório Excel
def gerar_relatorio_excel():
    workbook = xlsxwriter.Workbook('relatorio_frequencia_alunos.xlsx')
    worksheet = workbook.add_worksheet()

    headers = ['ID Aluno', 'Nome', 'Data', 'Turma', 'Presença']
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    alunos = get_students()
    row = 1

    for aluno in alunos:
        aluno_id = aluno[0]
        nome = aluno[1]
        frequencias = get_absences_by_student(aluno_id)

        for freq in frequencias:
            worksheet.write(row, 0, aluno_id)
            worksheet.write(row, 1, nome)
            worksheet.write(row, 2, freq[1])  # Data
            worksheet.write(row, 3, freq[2])  # Turma
            worksheet.write(row, 4, 'Presente' if freq[3] else 'Ausente')
            row += 1

    workbook.close()
    messagebox.showinfo('Sucesso', 'Relatório Excel gerado com sucesso!')


# Função que alterna entre as funcionalidades
def control(i):
    for widget in frameDir.winfo_children():
        widget.destroy()

    if i == 'novo_aluno':
        novo_aluno()
    if i == 'ver_alunos':
        ver_alunos()
    if i == 'registrar_presenca':
        registrar_presenca()
    if i == 'ver_frequencia':
        ver_frequencia()
    if i == 'gerar_relatorio_excel':
        gerar_relatorio_excel()


# Função para abrir a interface gráfica com os botões
def abrir_interface():
    Label(frameEsq, text="Opções", font=("Arial", 16), bg='#f0f0f5').pack(pady=20)

    Button(frameEsq, text="Adicionar Aluno", command=lambda: control('novo_aluno'), bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE).pack(pady=10)
    Button(frameEsq, text="Registrar Presença", command=lambda: control('registrar_presenca'), bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE).pack(pady=10)
    Button(frameEsq, text="Exibir Alunos", command=lambda: control('ver_alunos'), bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE).pack(pady=10)
    Button(frameEsq, text="Ver Frequência", command=lambda: control('ver_frequencia'), bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE).pack(pady=10)
    Button(frameEsq, text="Gerar Relatório em Excel", command=lambda: control('gerar_relatorio_excel'), bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE).pack(pady=10)
    Button(frameEsq, text="Sair", command=janela.quit, bg='#4CAF50', fg='white', font=('Ivy 11'), relief=GROOVE).pack(pady=20)


# Chamada para abrir a interface
abrir_interface()
janela.mainloop()
