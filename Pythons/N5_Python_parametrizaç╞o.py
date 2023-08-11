
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')


# --------------------------- FUNÇÃO QUE PEGA OS VALORES NAS JANELAS DE TEXTO E GRAVA NO ARQUIVO
def gravar_valor():
    val1 = valor1.get() # variável valor que recebe o valor digitado em env
    val2 = valor2.get()
    val3 = valor3.get() # variável valor que recebe o valor digitado em env
    
    arquivo_txt = "comandos.txt" # está dando nome para o arquivo txt
    s = open (arquivo_txt,'w')
    s.write(val1+"\n")

    s.write(val2+"\n")
    #s.write("0\n")

    s.write(val3+"\n")

    s.write("0\n")

    s.close()

#----------------------------- CRIAÇAO DA JENLA PRINCIPAL ---------------------
raiz=Tk() #criando a tela principal , usando um objeto TKinter
raiz.title("CONEXÃO SOCKET") #funcao para alterar titulo da janela
raiz.geometry('1000x500') #define o tamanho da janela
raiz.resizable(0, 0) #deixa o tamanho da janela fixo, sem opções de redimensionamento

#----------------------------- CRIA janela EXIBIÇÃO -------------------
janela = Frame(master=raiz,borderwidth=1, relief='sunken') #cria um janela no rodapé da janela, define como master a janela principal(raiz)
janela.place(x=10,y=10,width=980,height=480) #posiciona e define o tamanho dos janelas

label_exp = Label(janela, font=("Arial", 14, "bold"),text = "RoA Socket",padx=5,pady=5)
label_exp.place(x=650, y=5)

# TEXTO AO LADO DAS ENTRADAS DE TEXTO
comandos = Label(janela, font=("Arial", 14, "bold"),text = "ENTRAR COMANDOS",padx=5,pady=5)
comandos.place(x=40, y=60)

texto_valor1 = Label(janela, text = "LED Verde")
texto_valor1.place(x=20,y=120)
texto_valor1 = Label(janela, text = "Valor = 0 --> TX  |  Valor = 1 --> LED Acende")
texto_valor1.place(x=20,y=150)

texto_valor2 = Label(janela, text = "LED Amarelo")
texto_valor2.place(x=20,y=200)
texto_valor2 = Label(janela, text = "Valor = 0 --> Apagado | Valor = 1 --> Acende")
texto_valor2.place(x=20,y=230)

texto_valor3 = Label(janela, text = "LED Vermelho")
texto_valor3.place(x=20,y=280)
texto_valor3 = Label(janela, text = "Valor = 0 --> RX  |  Valor = 1 --> Acende  ")
texto_valor3.place(x=20,y=310)

# JANELAS DE ENTRA DOS VALORES COMEÇA COM ZERO
valor1=Entry(janela, width=10)
valor1.place(x=150,y=120)
valor1.insert(0, "0")

valor2=Entry(janela, width=10)
valor2.place(x=150,y=200)
valor2.insert(0, "0")

valor3=Entry(janela, width=10)
valor3.place(x=150,y=280)
valor3.insert(0, "0")

# CRIA BOTÃO PARA GRAVAR
botao=Button(janela,text="GRAVAR COMANDOS",font=("Arial", 14, "bold"), width=20,command= gravar_valor)
botao.place(x=30,y=350)
botao.config(state="normal")

# COLOCA FIGURA
minha_imagem = PhotoImage(file="Figura_RoA_Socket.png")
img = minha_imagem

canvas1 = Canvas(janela)
canvas1.configure(height='450')
canvas1.configure(width='750')
canvas1.place(x=280,y=40)
canvas1.create_image(10,10,image=img,anchor=NW)

###---------------------- CÓDIGO PARA RODAR A APLICAÇÃO
raiz.mainloop()









