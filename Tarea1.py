from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self,master):
        self.ven = master
        self.ven.title('Tarea 1')
        ancho = 250
        alto = 200
        ventana_alto = self.ven.winfo_screenmmwidth()
        ventana_ancho = self.ven.winfo_screenmmwidth()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f'{ancho}x{alto}+{x+550}+{y+150}')
    
    def Inicio(self):
        Label(self.ven,text='Ingrese un numero').place(x=70,y=10)
        self.n1 = Entry(self.ven)
        self.n1.place(x=63,y=50)
        Button(self.ven,text='Enviar a la lista',command=self.Envia).place(x=80,y=100)
        Button(self.ven,text='Cerrar',command=self.Cerrar).place(x=100,y=140)
    
    def Cerrar(self):
        self.ven.destroy()
    
    def Envia(self):
        try:
            n1 = int(self.n1.get())
            self.n1.delete(0,END)
            self.ven.withdraw()
            otra = Toplevel(self.ven)
            Ventanados(otra,self.ven,n1)
        except ValueError:
            messagebox.showerror('Error','Introduce solo numeros')
            self.n1.delete(0,END)
    
class Ventanados():
    def __init__(self,master,ven,a):
        self.n1 = a
        self.dos = master
        self.dos.title('Tarea 1')
        ancho = 250
        alto = 200
        ventana_alto = self.dos.winfo_screenmmwidth()
        ventana_ancho = self.dos.winfo_screenmmwidth()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.dos.geometry(f'{ancho}x{alto}+{x+550}+{y+150}')
        Label(self.dos,text='Numeros').place(x=150,y=10)
        self.lista = Listbox(self.dos, height=10, width=15, bg='grey', activestyle="dotbox", fg="Black") 
        self.lista.place(x=10, y=10)
        Button(self.dos,text='Regresar',command=self.Regresar).place(x=155,y=40)
        self.ven = ven
        #----------------------------------------------------------------------
        for i in range(self.n1):
            self.lista.insert(self.lista.size(),self.n1)
    
    def Regresar(self):
        self.lista.delete(0,END)
        self.dos.destroy()
        self.ven.deiconify()
    
if __name__=='__main__':
    master = Tk()
    app = Principal(master)
    app.Inicio()
    master.mainloop()