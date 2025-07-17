import customtkinter as ctk

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

def add_tasks():
    tarefa = entrada.get()      # Adiciona as entradas na variável tarefa
    if tarefa.strip() != "":    # Se o espaço não estiver vazio, cria a tarefa
        new_task = ctk.CTkCheckBox(frame_tarefas, text=tarefa)    # Cria uma Checkbox nomeada com a tarefa
        new_task.pack(pady=2, anchor='w')   # Dimensões da Checkbox / alinha a esquerda
        tarefas.append(new_task)    # Adiciona a tarefa na lista "tarefas"
        entrada.delete(0, 'end')   # Limpa o campo de entrada


def remove_tasks():
    for tarefa in tarefas[:]:
        if tarefa.get() == 1:   # Checkbox marcada (1: MARCADA / 0: NÃO MARCADA)
            tarefa.destroy()    # Remove o widget da Checkbox
            tarefas.remove(tarefa)  # Remove o Checkbox da lista


# Criando a janela
app = ctk.CTk()     # Cria a janela do CUSTOMTKINTER
app.geometry('400x500')     # Promove regras de tamanho(comprimento|altura) da janela em pixels
app.title('To do list com customtkinter')   # Promove um título para a janela


# HEADER
titulo = ctk.CTkLabel(app, text='To-do list', font=('Arial Black', 24))
titulo.pack(pady=(20, 10))


# Área de entrada das tarefas
# PACK: inserir e alinhar widgets na tela. itens são adicionados de cima para baixo.
# PADY: espaçamento vertical.
# PADX: espaçamento horizontal.
# FILL='x': Vai ocupar todo o comprimento horizontal da janela.
frame_input = ctk.CTkFrame(app)
frame_input.pack(pady=10, padx=20, fill='x')
entrada = ctk.CTkEntry(frame_input, placeholder_text='Digite uma nova tarefa')
# Dimensões da área de entrada.
entrada.pack(pady=10, padx=10, fill='x')


# Botão de adicionar tarefa
# COMMAND: vai usar a função "add_task" para adicionar tarefas.
frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=5)
botao_add = ctk.CTkButton(frame_botoes, text='➕Adicionar tarefa', command=add_tasks, width=100)
botao_add.pack(side='left', pady=10, padx=15)


# Botão de remover tarefa
botao_remove = ctk.CTkButton(frame_botoes, text='❌Remover tarefa', command=remove_tasks, width=100)
botao_remove.pack(side='left', pady=10, padx=15)


# Lista que vai armazenar os objetos Checkbox
frame_tarefas = ctk.CTkScrollableFrame(app, width=400, height=350)
frame_tarefas.pack(pady=10, padx= 20, fill='both', expand=True)
tarefas = []


# Inicia a aplicação
app.mainloop()

