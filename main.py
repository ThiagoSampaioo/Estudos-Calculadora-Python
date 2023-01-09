# importando bibliotecas
from tkinter import *
from tkinter import ttk

# definindo cores universais para a aplicação
corPT = "#242323"    # cor preta
corBR = "#f5f7f5"    # cor branca
corAZ = "#171a3d"    # cor azul
corCZ = "#bbbcbf"    # cor cinz
corAM = "#e0ae22"    # cor amarela


#crinado tela com tkinter
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x255")
janela.config(bg=corPT)


# passando valor para tela 
todos_valores = ''
def valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)
valor_texto = StringVar()

 
#criando fuções

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))



#limpando a tela para receber o resultado
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


#criando tela para receber as operações
frame_tela = Frame(janela, width=235, height=50, bg=corAZ)
frame_tela.grid(row=0, column=0)

#criando corpo para receber os butões
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#criando label na tela para exibir as operações
app_label = Label(frame_tela, textvariable=valor_texto ,width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 18", bg=corAZ, fg=corBR )
app_label.place(x=0,y=0)

#criando butões 
b_Clean = Button(frame_corpo, command= limpar_tela, text="C", width=16, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_Clean.place(x=0,y=0)

b_CEM = Button(frame_corpo, command= lambda: valores('%'), text="%", width=7, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_CEM.place(x=117,y=0)

b_DIV = Button(frame_corpo, command= lambda: valores('/'), text="/", width=7, height=2,bg=corAM, fg=corBR, relief=RAISED, overrelief=RIDGE)
b_DIV.place(x=176,y=0)


b_7 = Button(frame_corpo, command= lambda: valores('7'), text="7", width=7, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_7.place(x=0,y=41)

b_8 = Button(frame_corpo, command= lambda: valores('8'), text="8", width=7, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_8.place(x=58,y=41)

b_9 = Button(frame_corpo, command= lambda: valores('9'), text="9", width=7, height=2,bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_9.place(x=117,y=41)

b_MULT = Button(frame_corpo, command= lambda: valores('*'), text="*", width=7, height=2,bg=corAM, fg=corBR, relief=RAISED, overrelief=RIDGE)
b_MULT.place(x=176,y=41)



b_4 = Button(frame_corpo, command= lambda: valores('4'), text="4", width=7, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_4.place(x=0,y=82)

b_5 = Button(frame_corpo, command= lambda: valores('5'), text="5", width=7, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_5.place(x=58,y=82)

b_6 = Button(frame_corpo, command= lambda: valores('6'), text="6", width=7, height=2,bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_6.place(x=117,y=82)

b_SUB = Button(frame_corpo, command= lambda: valores('-'), text="-", width=7, height=2,bg=corAM, fg=corBR, relief=RAISED, overrelief=RIDGE)
b_SUB.place(x=176,y=82)



b_1 = Button(frame_corpo, command= lambda: valores('1'), text="1", width=7, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=123)

b_2 = Button(frame_corpo, command= lambda: valores('2'), text="2", width=7, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_2.place(x=58,y=123)

b_3 = Button(frame_corpo, command= lambda: valores('3'), text="3", width=7, height=2,bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_3.place(x=117,y=123)

b_SOMA = Button(frame_corpo, command= lambda: valores('+'), text="+", width=7, height=2,bg=corAM, fg=corBR, relief=RAISED, overrelief=RIDGE)
b_SOMA.place(x=176,y=123)



b_0 = Button(frame_corpo, command= lambda: valores('0'), text="0",  width=16, height=2, bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_0.place(x=0,y=164)

b_VIR = Button(frame_corpo, command= lambda: valores(','), text=",", width=7, height=2,bg=corCZ, relief=RAISED, overrelief=RIDGE)
b_VIR.place(x=117,y=164)

b_IGUAL = Button(frame_corpo, command= calcular, text="=", width=7, height=2,bg=corAM, fg=corBR, relief=RAISED, overrelief=RIDGE)
b_IGUAL.place(x=176,y=164 )






janela.mainloop()
