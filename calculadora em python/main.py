#importar o tkinter     
from cProfile import label
import string
from tkinter import *
from tkinter import ttk
from turtle import right

#definindo cor do background
#definindo cores para  o display de resultados
cor1 = "#000000" #preto
cor2 = "#8503a6" #roxo
cor3 = "#8c8c8c" #cinza
cor4 = "#36db27" #verde
cor5 = "#1f2cde" #azul
cor6 = "#ffffff" #branca


janela=Tk()
janela.title("Calculadora")
janela.geometry("235x320")
janela.config(bg=cor1)


#criando frames
#display tela de resultado calculadora.
frame_tela = Frame(janela, width=250, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)


#segundo frame
frame_corpo = Frame(janela, width=250, height=268)
frame_corpo.grid(row=1, column=0)


#variavel todos valores
todos_valores=''


#criando label para função do botoes

valor_texto = StringVar()


#criando funções 
def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    


    #passando o valor para a tela
    valor_texto.set(todos_valores)

    #função para calcular 

def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""

#função para limpar 
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")



app_label = Label( frame_tela, textvariable=valor_texto,width=16,height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 18 '),bg=cor3,fg=cor6)
app_label.place(x=0,y=0)

#criando botões
b_1 = Button(frame_corpo, command=lambda: limpar_tela() ,text="C", width=12, height=2, bg=cor2,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('%'),text="%", width=5, height=2,bg=cor2,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('/'),text="/", width=5, height=2,bg=cor4, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_3.place(x=180, y=0)

b_4 = Button(frame_corpo, command=lambda:entrar_valores('7'),text="7", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command=lambda:entrar_valores('8'),text="8", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_5.place(x=60, y=52)
b_6 = Button(frame_corpo, command=lambda:entrar_valores('9'),text="9", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_6.place(x=120, y=52)
b_6a = Button(frame_corpo, command=lambda:entrar_valores('*'),text="*", width=5, height=2,bg=cor4, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_6a.place(x=180, y=52)

b_7 = Button(frame_corpo, command=lambda:entrar_valores('4'),text="4", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_7.place(x=0, y=104)
b_8 = Button(frame_corpo, command=lambda:entrar_valores('5'),text="5", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_8.place(x=60, y=104)
b_9 = Button(frame_corpo,command=lambda:entrar_valores('6'), text="6", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_9.place(x=120, y=104)
b_10 = Button(frame_corpo, command=lambda:entrar_valores('-'), text="-", width=5, height=2,bg=cor4, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)

b_10.place(x=180, y=104)
b_11 = Button(frame_corpo, command=lambda:entrar_valores('1'),text="1", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_11.place(x=0, y=155)
b_12 = Button(frame_corpo,command=lambda:entrar_valores('2'), text="2", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_12.place(x=60, y=155)
b_13 = Button(frame_corpo, command=lambda:entrar_valores('3'),text="3", width=5, height=2,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_13.place(x=120, y=155)
b_14 = Button(frame_corpo, command=lambda:entrar_valores('+'),text="+", width=5, height=2,bg=cor4, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_14.place(x=180, y=155)

b_15 = Button(frame_corpo, command=lambda:entrar_valores('0'),text="0", width=11, height=3,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_15.place(x=0, y=206)
b_16 = Button(frame_corpo, command=lambda:entrar_valores('.'),text=".", width=5, height=3,bg=cor2, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_16.place(x=120, y=206)
b_17 = Button(frame_corpo, command=lambda:calcular() ,text="=", width=5, height=3,bg=cor4, fg=cor6,font=('Ivy 12 bold'), relief=RAISED,overrelief=RIDGE)
b_17.place(x=180, y=206)






janela.mainloop()

