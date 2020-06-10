from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

nomearquivo = None

def novoArquivo():
    global nomearquivo
    nomearquivo = "Sem-Título"
    texto.delete(0.0, END)

def SalvarArquivo():
    global nomearquivo
    t = texto.get(0.0, END)
    f = open(nomearquivo, 'w')
    f.write(t)
    f.close()

def salvarComo():
    f = asksaveasfile(mode = 'w', defaultextension='.txt')
    t = texto.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="OPA VISH TRETA", message="Incapaz de salvar isso daí ¯\_(ツ)_/¯")

def abrirArquivo():
    f = askopenfile(mode='r')
    t = f.read()
    texto.delete(0.0, END)
    texto.insert(0.0, t)

root = Tk()
root.title("Editor de texto com Python")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

texto = Text(root, width=400, height=400)
texto.pack()

barramenu = Menu(root)
menuarquivo = Menu(barramenu)
menuarquivo.add_command(label="Novo", command=novoArquivo)
menuarquivo.add_command(label="Abrir", command=abrirArquivo)
menuarquivo.add_command(label="Salvar Como...", command=salvarComo)
menuarquivo.add_separator()
menuarquivo.add_command(label="Sair", command=root.quit)
barramenu.add_cascade(label="Arquivo", menu=menuarquivo)

root.config(menu=barramenu)
root.mainloop()


