from tkinter import * 
from tkinter import messagebox

class Ventana():
    def __init__(self,master):
        self.ven = master
        self.ven.title('Programa 1')
        ancho = 250
        alto = 200
        ventana_alto = self.ven.winfo_screenmmwidth()
        ventana_ancho = self.ven.winfo_screenmmwidth()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f'{ancho}x{alto}+{x+550}+{y+150}')
        #------------------------------------------------------

    def Inicio(self):
        Label(self.ven,text='Escribe un numero').place(x=50,y=20)
        self.n1 = Entry(self.ven)
        self.n1.place(x=50,y=50)
        Label(self.ven,text='Escribe un numero').place(x=50,y=75)
        self.n2 = Entry(self.ven)
        self.n2.place(x=50,y=100)
        Button(self.ven,text='Enviar',command=self.Enviar,width=10).place(x=25,y=130)
        Button(self.ven,text='Cerrar',command=self.Cerrar,width=10).place(x=130,y=130)

    def Enviar(self):
        try:
            n1 = int(self.n1.get())
            n2 = int(self.n2.get())
            self.n1.delete(0,END)
            self.n2.delete(0,END)
            self.ven.withdraw()
            otra = Toplevel(self.ven)
            Ventanados(otra,self.ven,n1,n2)
        except ValueError:
            self.n1.delete(0,END)
            self.n2.delete(0,END)
            messagebox.showerror('Erorr','Algun dato no es numero')

    def Cerrar(self):
        self.ven.destroy()

class Ventanados():
    def __init__(self,master,ven,a,b):
        self.n1 = a
        self.n2 = b
        self.dos = master
        self.dos.title('Programa 1')
        ancho = 250
        alto = 200
        ventana_alto = self.dos.winfo_screenmmwidth()
        ventana_ancho = self.dos.winfo_screenmmwidth()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.dos.geometry(f'{ancho}x{alto}+{x+550}+{y+150}')
        Label(self.dos,text='Hola mundo').place(x=50,y=50)
        Button(self.dos,text='Regresar',command=self.Regresar).place(x=50,y=100)
        self.ven = ven
        Button(self.dos,text='Sumar',command=self.sumar).place(x=150,y=100)
    
    def sumar(self):
        messagebox.showinfo('La suma',f'La suma de {self.n1} mas {self.n2} es \n {self.n1 + self.n2}')
    def Regresar(self):
        self.dos.destroy()
        self.ven.deiconify()

if __name__ == '__main__':
    master = Tk()
    app = Ventana(master)
    app.Inicio()
    master.mainloop()