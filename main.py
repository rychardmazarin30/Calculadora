# Bibliotecas importadas
from tkinter import *
from tkinter import ttk

# CORES
blackColor = '#000000'
whiteColor = '#feffff'
blueColor = '#38576b'
cinza = '#ECEFF1'
orangeColor = '#FFAB40'

# Criando interface da CALCULADORA
janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg = blueColor)

# Criando Frames
frame_tela = Frame(janela, width = 235, height = 50, bg = blueColor)
frame_tela.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width = 235, height = 268)
frame_corpo.grid(row = 1, column = 0)

# Variavel all values
all_values = ""

# Criando label 
text_value = StringVar()

# Criando funções
def  entrar_valores(event):
    global all_values
    all_values = all_values + str(event)
    # Passando valores para tela 
    text_value.set(all_values)

def calcular():
    global all_values
    resultado = eval(all_values)
    
    text_value.set(str(resultado))

def limparTela():
    global all_values
    all_values = ""
    text_value.set("")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

app_label = Label(frame_tela, 
textvariable = text_value, width=16, height=2, 
padx = 7, relief = FLAT, anchor = 'e', justify = RIGHT, font = ('Ivy 18'), bg = blueColor, fg = whiteColor)
app_label.place(x = 0, y = 0)

# Botões

botao_1 = Button(frame_corpo, command = limparTela,
 text= "C", width = 11, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_1.place(x=0, y=0)

botao_2 = Button(frame_corpo, 
command = lambda: entrar_valores('%'),
text= "%", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_2.place(x=118, y=0)

botao_3 = Button(frame_corpo, 
command = lambda: entrar_valores('/'),
text= "/", width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_3.place(x=177, y=0)

botao_4 = Button(frame_corpo, 
command = lambda: entrar_valores('7'),
text= "7", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_4.place(x=0, y=52)

botao_5 = Button(frame_corpo, 
command = lambda: entrar_valores('8'),
text= "8", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_5.place(x=59, y=52)

botao_6 = Button(frame_corpo, 
command = lambda: entrar_valores('9'),
text= "9", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_6.place(x=118, y=52)

botao_7 = Button(frame_corpo, 
command = lambda: entrar_valores('*'),
text= "*", width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_7.place(x=177, y=52)

botao_8 = Button(frame_corpo, 
command = lambda: entrar_valores('4'),
text= "4", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_8.place(x=0, y=104)

botao_9 = Button(frame_corpo, 
command = lambda: entrar_valores('5'),
text= "5", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_9.place(x=59, y=104)

botao_10 = Button(frame_corpo, 
command = lambda: entrar_valores('6'),
text= "6", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_10.place(x=118, y=104)

botao_11 = Button(frame_corpo, 
command = lambda: entrar_valores('-'),
text= "-", width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_11.place(x=177, y=104)

botao_12 = Button(frame_corpo, 
command = lambda: entrar_valores('1'),
text= "1", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_12.place(x=0, y=156)

botao_13 = Button(frame_corpo, 
command = lambda: entrar_valores('2'),
text= "2", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_13.place(x=59, y=156)

botao_14 = Button(frame_corpo, 
command = lambda: entrar_valores('3'),
text= "3", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_14.place(x=118, y=156)

botao_15 = Button(frame_corpo, 
command = lambda: entrar_valores('+'),
text= "+", width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_15.place(x=177, y=156)

botao_16 = Button(frame_corpo,
command = lambda: entrar_valores('0'),
 text= "0", width = 11, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_16.place(x=0, y=208)

botao_17 = Button(frame_corpo, 
command = lambda: entrar_valores('.'),
text= ".", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_17.place(x=118, y=208)

botao_18 = Button(frame_corpo, command = calcular,
text= "=", width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief= RIDGE)
botao_18.place(x=177, y=208)

janela.mainloop()
