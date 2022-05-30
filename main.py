from tkinter import *
from tkinter import ttk

# Colors
white = '#FFFFFF'
darkBlack = '#080707'
orange = '#d47d13'
black = '#383636' 
white2 = '#78756c'

j = Tk()
j.title('Calculadora')
j.geometry('300x450')
j.config(bg=darkBlack)

# Frames
frame_tela = Frame(j, width=280, height=102, bg=black, relief='raised')
frame_tela.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_botoes = Frame(j, width=335, height=400, bg=darkBlack, relief='flat')
frame_botoes.grid(row=1, column=0, sticky=NW)

all_values = ""
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
    all_values = ""
    
    text_value.set(str(resultado))
   
def limparTela():
    global all_values
    all_values = ""
    text_value.set("")

def limpar_ultimo():
    global all_values
    all_values = all_values[:-1]
    text_value.set(all_values)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

label_tela = Label(
        frame_tela,
        textvariable = text_value,
        width=17,
        height=5,
        padx = 7,
        relief = FLAT,
        anchor = 'e',
        justify = RIGHT,
        font = ('Ivy 20'),
        bg = darkBlack,
        fg = white )
label_tela.place(x=0, y=0)

# Configurando os botões
b_C = Button(
        frame_botoes,
        command= limparTela,
        text= "C",
        width = 5,
        height = 2,
        bg = white2,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_C.place(x=82, y=1)

b_mais_ou_menos = Button(
        frame_botoes,
        command= limpar_ultimo,
        text= "CE",
        width = 5,
        height = 2,
        bg = white2,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_mais_ou_menos.place(x=10, y=1)

b_rest = Button(
        frame_botoes,
        command= lambda: entrar_valores('%'),
        text= "%",
        width = 5,
        height = 2,
        bg = white2,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_rest.place(x=156, y=1)

b_div = Button(
        frame_botoes,
        text= "/",
        command= lambda: entrar_valores('/'),
        width = 5,
        height = 2,
        bg = orange,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_div.place(x=230, y=2)

b_7 = Button(
        frame_botoes,
        command= lambda: entrar_valores('7'),
        text= "7",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_7.place(x=10, y=65)

b_8 = Button(
        frame_botoes,
        command= lambda: entrar_valores('8'),
        text= "8",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_8.place(x=82, y=65)

b_9 = Button(
        frame_botoes,
        command= lambda: entrar_valores('9'),
        text= "9",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_9.place(x=156, y=65)

b_mult = Button(
        frame_botoes,
        command= lambda: entrar_valores('*'),
        text= "X",
        width = 5,
        height = 2,
        bg = orange,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_mult.place(x=230, y=65)

b_4 = Button(
        frame_botoes,
        command= lambda: entrar_valores('4'),
        text= "4",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_4.place(x=10, y=129)

b_5 = Button(
        frame_botoes,
        command= lambda: entrar_valores('5'),
        text= "5",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_5.place(x=82, y=129)

b_6 = Button(
        frame_botoes,
        command= lambda: entrar_valores('6'),
        text= "6",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_6.place(x=156, y=129)

b_sub = Button(
        frame_botoes,
        command= lambda: entrar_valores('-'),
        text= "-",
        width = 5,
        height = 2,
        bg = orange,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_sub.place(x=230, y=129)

b_1 = Button(
        frame_botoes,
        command= lambda: entrar_valores('1'),
        text= "1",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_1.place(x=10, y=193)

b_2 = Button(
        frame_botoes,
        command= lambda: entrar_valores('2'),
        text= "2",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_2.place(x=82, y=193)

b_3 = Button(
        frame_botoes,
        command= lambda: entrar_valores('3'),
        text= "3",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_3.place(x=156, y=193)

b_soma = Button(
        frame_botoes,
        command= lambda: entrar_valores('+'),
        text= "+",
        width = 5,
        height = 2,
        bg = orange,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_soma.place(x=230, y=193)

b_0 = Button(
        frame_botoes,
        command= lambda: entrar_valores('0'),
        text= "0",
        width = 12,
        height = 2,
        anchor= 'center',
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_0.place(x=10, y=257)

b_point = Button(
        frame_botoes,
        command= lambda: entrar_valores('.'),
        text= ".",
        width = 5,
        height = 2,
        bg = black,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_point.place(x=156, y=257)

b_igual = Button(
        frame_botoes,
        command= calcular,
        text= "=",
        width = 5,
        height = 2,
        bg = orange,
        fg=white,
        font = ('Ivy 13 bold'),
        relief = RAISED,
        overrelief= RIDGE)
b_igual.place(x=230, y=257)


j.mainloop()
