import tkinter as tk
from tkinter import TclError, messagebox
import sqlite3

##### INTERFACE #####

###cores###
vinho = "#993399"
roxo = "#8f3399"
verdeAgua = "#40E0D0"
azulPiscina = "#00FFFF"

###leiaute###
janela = tk.Tk()
janela.geometry('710x400')
janela.resizable(width=tk.FALSE, height=tk.FALSE) #impossivel alterar tamanho
janela.title('Agenda de Contatos')
janela.configure(background=roxo)

###variaveis dos campos de texto###
inputNome = tk.StringVar()      #
inputSobrenome = tk.StringVar() #  } inserir
inputTelefone = tk.StringVar()  # 
radioNome = tk.BooleanVar()         #
radioSobrenome = tk.BooleanVar()    #
radioTelefone = tk.BooleanVar()     # }buscar
buscarNome = tk.StringVar()         #
buscarSobrenome = tk.StringVar()    #
buscarTelefone = tk.StringVar()     #

########## FRAMES ##########
#frame_esquerda
frame_esquerda=tk.Frame(janela, width = 290, height=400, relief="flat", bg=azulPiscina)
frame_esquerda.grid(row=0, column=0, sticky=tk.NW)

frame_esquerda_cima=tk.Frame(frame_esquerda, width = 10, height=35, relief="flat", bg=azulPiscina)
frame_esquerda_cima.grid(row=0, column=0, sticky=tk.NSEW)

frame_esquerda_meio=tk.Frame(frame_esquerda, width = 10, height=345, relief="flat", bg=azulPiscina)
frame_esquerda_meio.grid(row=2, column=0, sticky=tk.NSEW)

frame_esquerda_baixo=tk.Frame(frame_esquerda, width =10, height=35, relief="flat", bg=azulPiscina)
frame_esquerda_baixo.grid(row=3, column=0, sticky=tk.NSEW)

#botões
b_novo=tk.Button(frame_esquerda_cima,text="NOVO",width=8,height=1,bg=vinho, fg="black",anchor="center",relief=tk.RAISED)
b_novo.grid(row=0,column=0,sticky=tk.NSEW,pady=1)

b_remover=tk.Button(frame_esquerda_cima,text="REMOVER",width=10,height=1,bg=vinho, fg="black",anchor="center",relief=tk.RAISED,state=tk.DISABLED)
b_remover.grid(row=0,column=1,sticky=tk.NSEW,pady=1)

b_editar=tk.Button(frame_esquerda_cima,text="EDITAR",width=8,height=1,bg=vinho, fg="black",anchor="center",relief=tk.RAISED,state=tk.DISABLED)
b_editar.grid(row=0,column=2,sticky=tk.NSEW,pady=1)

b_buscar=tk.Button(frame_esquerda_cima,text="BUSCAR",width=10,height=1,bg=vinho, fg="black",anchor="center",relief=tk.RAISED)
b_buscar.grid(row=0,column=3,sticky=tk.NSEW,pady=1)

b_ok=tk.Button(frame_esquerda_baixo,text="CADASTRAR",width=10,height=1,bg=verdeAgua, fg="black",anchor="center",relief=tk.RAISED,state=tk.DISABLED)
b_ok.grid(row=0,column=4,sticky=tk.W,pady=1,padx=105)

#frame_meio
frame_meio=tk.Frame(janela, width = 300, height=400, bg=azulPiscina, relief="flat")
frame_meio.grid(row=0, column=1, sticky=tk.NSEW)

b_contatos=tk.Button(frame_meio,text="CONTATOS", width=10,height=1,bg=roxo,fg="black",anchor="center", relief=tk.RAISED)
b_contatos.grid(row=0,column=0,sticky=tk.NSEW,pady=1,padx=1)

listaContatos = tk.Listbox(frame_meio, bg=roxo, height=30, width=41, selectmode=tk.SINGLE)
scrollLista = tk.Scrollbar(frame_meio)#, background=azulPiscina, activebackground=verdeAgua) NÃO FUNCIONOu
listaContatos.grid(row=1, column=0)
scrollLista.grid(row=1,column=1,ipady=161,sticky="N")

#frame_direita
frame_direita=tk.Frame(janela, width = 150, height=400, bg=azulPiscina, relief="flat")
frame_direita.grid(row=0, column=2, sticky=tk.NSEW)

b_alfCresc=tk.Button(frame_direita,text="A ~ Z",width=20,height=1,bg=verdeAgua,fg="black",anchor="center",relief=tk.RAISED)
b_alfCresc.grid(row=0,column=0,sticky=tk.NSEW,pady=1,padx=1)

b_alfDecresc=tk.Button(frame_direita,text="Z ~ A",width=20,height=1,bg=verdeAgua,fg="black",anchor="center",relief=tk.RAISED)
b_alfDecresc.grid(row=1,column=0,sticky=tk.NSEW,pady=1,padx=1)

b_limpar=tk.Button(frame_direita,text="LIMPAR",width=20,height=1,bg=verdeAgua,fg="black",anchor="center",relief=tk.RAISED)
b_limpar.grid(row=2,column=0,sticky=tk.NSEW,pady=1,padx=1)

labelPreencher = tk.Label(frame_direita,text="",bg=azulPiscina).grid(row=3,pady=120)

b_apagar=tk.Button(frame_direita,text="APAGAR TODOS OS DADOS",width=20,height=1,bg=verdeAgua,fg="black",anchor="center",relief=tk.RAISED)
b_apagar.grid(row=4,column=0,sticky=tk.NSEW,pady=1,padx=1)

b_sair=tk.Button(frame_direita,text="SAIR",width=20,height=1,bg=verdeAgua, fg="black",anchor="center",relief=tk.RAISED)
b_sair.grid(row=5,column=0,sticky=tk.NSEW,pady=1,padx=1)


###inserir###
labelNome = tk.Label(frame_esquerda_meio, text="Nome:", width=10, height=1, fg="black",anchor="center", relief="flat",bg=azulPiscina)
labelSobrenome = tk.Label(frame_esquerda_meio, text="Sobrenome:", width=10, height=1, fg="black",anchor="center", relief="flat",bg=azulPiscina)
labelTelefone = tk.Label(frame_esquerda_meio, text="Telefone com DDD:", width=15,fg="black", anchor="center", relief="flat", bg=azulPiscina)
labelPreencher0 = tk.Label(frame_esquerda_meio,text="",bg=azulPiscina)
labelPreencher1 = tk.Label(frame_esquerda_meio,text="",bg=azulPiscina)

tfNome = tk.Entry(frame_esquerda_meio, textvariable=inputNome)
tfSobrenome = tk.Entry(frame_esquerda_meio, textvariable=inputSobrenome)
tfTelefone = tk.Entry(frame_esquerda_meio, textvariable=inputTelefone)
tfNome.focus()
tfSobrenome.focus()
tfTelefone.focus()

b_cancelar=tk.Button(frame_esquerda_meio,text="CANCELAR", width=10,height=1,bg=verdeAgua,fg="black",anchor="center", relief=tk.RAISED)#.place(x=150,y=150)


##### BANCO DE DADOS #####
conexao = sqlite3.connect('contatos.db')
cursor = conexao.cursor()
#conectado = True
conexao.execute('CREATE TABLE IF NOT EXISTS lista(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, telefone TEXT)')
conexao.commit()

"""def desconectar(self):
    conexao.close()
    self.conectado = False
    return conectado

def conectar(self):
    conexao.cursor()
    self.conectado = True
    return conectado"""

def fetchall():
    return cursor.fetchall()  # buscar todos

def confirmar():
    #if conectado:
    conexao.commit()  # confirmar alteração
    #    return True
    #else:
    #    return False

def ver():
    cursor.execute('SELECT * FROM lista')
    rows = fetchall()
    return rows

def inserir(nome, sobrenome, telefone):
    cursor.execute('INSERT INTO lista(nome,sobrenome,telefone) VALUES (?,?,?)',(nome,sobrenome,telefone))
    confirmar()

def buscar_nome(nome):
    cursor.execute('SELECT * FROM lista WHERE nome=?',(nome,))
    rows = fetchall()
    return rows
    
def buscar_sobrenome(sobrenome):
    cursor.execute('SELECT * FROM lista WHERE sobrenome=?',(sobrenome,))
    rows = fetchall()
    return rows

def buscar_telefone(telefone):
    cursor.execute('SELECT * FROM lista WHERE telefone=?',(telefone,))
    rows = fetchall()
    return rows

def editar(nome="", sobrenome="", telefone="", id=""):
    cursor.execute('UPDATE lista SET nome=?,sobrenome=?,telefone=? WHERE id=?',(nome,sobrenome,telefone,id))
    confirmar()

def deletar(id):
    cursor.execute('DELETE FROM lista WHERE id =?',(id,))
    confirmar()

def apagar():
    cursor.execute('DROP TABLE lista')

def nova_tabela():
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS lista(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, telefone TEXT)')
    conexao.commit()

def asc():
    cursor.execute('SELECT * FROM lista ORDER BY nome ASC')
    resultado = fetchall()
    return resultado
def desc():
    cursor.execute('SELECT * FROM lista ORDER BY nome DESC')
    resultado = fetchall()
    return resultado

##### MÉTODOS #####
def get_linha_selecionada(event):
    comando_inserir()
    global selecionado
    index = listaContatos.curselection()
    selecionado = listaContatos.get(index)
    tfNome.delete(0, 'end')
    tfNome.insert('end', selecionado[1])
    tfSobrenome.delete(0, 'end')
    tfSobrenome.insert('end', selecionado[2])
    tfTelefone.delete(0, 'end')
    tfTelefone.insert('end', selecionado[3])
    b_editar['state']=tk.NORMAL
    b_remover['state']=tk.NORMAL

listaContatos.bind('<<ListboxSelect>>', get_linha_selecionada)

#esconder TELAS
def aparecer_campos():
    labelPreencher0.grid(row=0,column=0,sticky=tk.NSEW,pady=20,padx=1)

    labelNome.grid(row=4,column=0,sticky=tk.NSEW,pady=1,padx=1)
    labelSobrenome.grid(row=5,column=0,sticky=tk.NSEW,pady=1,padx=1)
    labelTelefone.grid(row=6,column=0,sticky=tk.NSEW,pady=1,padx=1)

    tfNome.grid(row=4,column=1,sticky=tk.NSEW,pady=1,padx=1)
    tfSobrenome.grid(row=5,column=1,sticky=tk.NSEW,pady=1,padx=1)
    tfTelefone.grid(row=6,column=1,sticky=tk.NSEW,pady=1,padx=1)
    tfNome.config(textvariable=inputNome)
    tfSobrenome.config(textvariable=inputSobrenome)
    tfTelefone.config(textvariable=inputTelefone)

    b_cancelar.grid(row=7,column=1,sticky=tk.NSEW,pady=15,padx=1)

    labelPreencher1.grid(row=8,column=0,sticky=tk.NSEW,pady=69,padx=1)
def esconder_campos():
    labelNome.grid_forget()
    labelSobrenome.grid_forget()
    labelTelefone.grid_forget()
    tfNome.grid_forget()
    tfSobrenome.grid_forget()
    tfTelefone.grid_forget()
    b_cancelar.grid_forget()


def botao_ok():
    b_ok.grid(row=0,column=4,sticky=tk.W,pady=1,padx=105)
    b_ok['state']=tk.NORMAL

def botao_ver_desativar():
    b_novo['state']=tk.NORMAL
    b_remover['state']=tk.DISABLED
    b_editar['state']=tk.DISABLED
    b_buscar['state']=tk.DISABLED
    b_contatos['state']=tk.DISABLED
    b_alfCresc['state']=tk.DISABLED
    b_alfDecresc['state']=tk.DISABLED
    b_apagar['state']=tk.DISABLED
    b_limpar['state']=tk.DISABLED
def botao_ver_ativar():
    b_buscar['state']=tk.NORMAL
    b_contatos['state']=tk.NORMAL
    b_alfCresc['state']=tk.NORMAL
    b_alfDecresc['state']=tk.NORMAL
    b_apagar['state']=tk.NORMAL
    b_limpar['state']=tk.NORMAL


##### COMANDOS #####
def comando_inserir():
    aparecer_campos()
    nova_tabela()
    botao_ok()
    
    tfNome.delete(0, 'end')         #
    tfSobrenome.delete(0, 'end')    # } apaga as caixas de texto anteriores
    tfTelefone.delete(0,'end')      #

def comando_ver():
    listaContatos.delete(0, 'end')
    rows = ver()
    for r in rows:
        listaContatos.insert('end', r)

    if len(rows) == 0:
        messagebox.showwarning(title='Ooops!',message='Nenhum contato a exibir.')
        botao_ver_desativar()
        comando_inserir()
    else:
        botao_ver_ativar()

def comando_ok():
    if len(tfNome.get()) == 0 or len(tfSobrenome.get())==0 or len(tfTelefone.get())==0:
        messagebox.showwarning(title='Algo não está certo...', message='Por favor preencha todos os campos')
    else:
        messagebox.showinfo(title='Uhuuuu',message='Contato cadastrado com sucesso!!')
        messagebox.showinfo(title='INPUT',message='\tNOVO CONTATO ADICIONADO!\n\nNome: '+tfNome.get()+' '+tfSobrenome.get()+'\nTelefone: '+tfTelefone.get())
        inserir(tfNome.get(),tfSobrenome.get(),tfTelefone.get())
        botao_ver_ativar()
        esconder_campos()
        labelPreencher0.grid(row=0,column=0,sticky=tk.NSEW,pady=83,padx=1)
        b_ok['state']=tk.DISABLED
        comando_ver()

def comando_buscar():
    if len(tfNome.get())== 0 and len(tfSobrenome.get())==0 and len(tfTelefone.get())==0:
        messagebox.showerror(title='ERROR',message='Nenhum dado a buscar. Por favor insira algo')
        aparecer_campos()
    else:
        if len(tfNome.get()) != 0:
            listaContatos.delete(0, 'end')
            row=buscar_nome(tfNome.get())
            for r in row:
                listaContatos.insert(tk.END, r)
            if len(row) ==0:
                messagebox.showwarning(title='Oops',message='Nenhum contato com este nome')
        if len(tfSobrenome.get()) !=0:
            listaContatos.delete(0, 'end')
            row=buscar_sobrenome(tfSobrenome.get())
            for r in row:
                listaContatos.insert(tk.END, r)
            if len(row) ==0:
                messagebox.showwarning(title='Oops',message='Nenhum contato com este sobrenome')
        if len(tfTelefone.get()) !=0:
            listaContatos.delete(0, 'end')
            row=buscar_telefone(tfTelefone.get())
            for r in row:
                listaContatos.insert(tk.END, r)
            if len(row) ==0:
                messagebox.showwarning(title='Oops',message='Nenhum contato com este telefone')

def comando_cancelar():
    esconder_campos() #apaga a tela do botão 'novo'
    labelPreencher0.grid(row=0,column=0,sticky=tk.NSEW,pady=83,padx=1) #preenche espaço que então fica vazio
    b_ok['state']=tk.DISABLED
   # b_okBuscar['state']=tk.DISABLED

    #apagar dados dos campos de texto
    tfNome.delete(0, 'end')
    tfSobrenome.delete(0, 'end')
    tfTelefone.delete(0,'end')


def comando_editar():
    if not listaContatos.curselection():
        messagebox.showerror(title='ERRO',message='Selecione um contato para editar')
    else:
        editar(tfNome.get(),tfSobrenome.get(),tfTelefone.get(),selecionado[0])
    listaContatos.delete(0, 'end')
    rows = ver()
    for r in rows:
        listaContatos.insert('end', r)
    b_remover['state']=tk.DISABLED
    b_editar['state']=tk.DISABLED
    
def comando_remover():
    if not listaContatos.curselection():
        messagebox.showerror(title='ERRO',message='Selecione um contato para remover')
    else:
        listaContatos.delete(listaContatos.curselection())
        id = selecionado[0]
        deletar(id)

        #tfNome.delete(0, 'end')
        #tfSobrenome.delete(0, 'end')
        #tfTelefone.delete(0,'end')
    listaContatos.delete(0, 'end')
    rows = ver()
    for r in rows:
        listaContatos.insert('end', r)
    b_remover['state']=tk.DISABLED
    b_editar['state']=tk.DISABLED

def comando_alfcresc():
    b_alfCresc['state']=tk.DISABLED #não pode clicar novamente para não ficar aparecendo várias vezes
    listaContatos.delete(0, 'end')

    resultado=asc()
    
   # if sqlite3.OperationalError:
    if len(resultado) == 0:
        botao_ver_desativar()
        messagebox.showwarning(title='Ooops!',message='Nenhum contato a exibir.')
        comando_inserir()
    else:
        for linha in resultado:
            listaContatos.insert(tk.END, linha)
        botao_ver_ativar()
def comando_alfdecresc():
    b_alfDecresc['state']=tk.DISABLED
    listaContatos.delete(0, 'end')

    resultado=desc()
    
    if len(resultado) == 0:#if sqlite3.OperationalError:
        botao_ver_desativar()
        messagebox.showwarning(title='Ooops!',message='Nenhum contato a exibir.')
        comando_inserir()
    else:
        for linha in resultado:
            listaContatos.insert(tk.END, linha)
        botao_ver_ativar()

def comando_limpar():
    listaContatos.delete(0, 'end')
    tfNome.delete(0, 'end')
    tfSobrenome.delete(0, 'end')
    tfTelefone.delete(0,'end')
    b_alfCresc['state']=tk.NORMAL
    b_alfDecresc['state']=tk.NORMAL

def comando_apagar():
    prosseguir=messagebox.askquestion(title='Isso é perigoso!',message='Você está prestes à excluir permanentemente TODA sua lista de contatos. Deseja prosseguir?')
    if prosseguir == 'yes':
        apagar()
        listaContatos.delete(0, 'end')

###dando poder aos botões###
b_novo.configure(command=comando_inserir)
b_remover.configure(command=comando_remover)
b_editar.configure(command=comando_editar)
b_buscar.configure(command=comando_buscar)
b_contatos.configure(command=comando_ver)
b_ok.configure(command=comando_ok)
b_cancelar.configure(command=comando_cancelar)
b_alfCresc.configure(command=comando_alfcresc)
b_alfDecresc.configure(command=comando_alfdecresc)
b_limpar.configure(command=comando_limpar)
b_apagar.configure(command=comando_apagar)
b_sair.configure(command=janela.destroy)

janela.mainloop()