from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3

def crearBaseDatos():
    con = sqlite3.connect("Usuarios.db")
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,password TEXT NOT NULL)""")

    cursor.execute("SELECT * FROM usuarios WHERE usuario='admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (usuario,password) VALUES (?,?)",("admin","12345"))

    con.commit()
    con.close()

class Ventana():
    def __init__(self,master):
        self.ven = master
        self.ven.title('Programa 2')
        ancho = 250
        alto = 200
        ventana_ancho = self.ven.winfo_screenwidth()
        ventana_alto = self.ven.winfo_screenheight()
        x = (ventana_ancho // 2) - (ancho // 2)
        y = (ventana_alto // 2) - (alto // 2)
        self.ven.geometry(f'{ancho}x{alto}+{x}+{y}')

    def Inicio(self):
        Label(self.ven,text='Usuario').place(x=50,y=20)
        self.n1 = Entry(self.ven)
        self.n1.place(x=50,y=50)

        Label(self.ven,text='Password').place(x=50,y=75)
        self.n2 = Entry(self.ven, show="*")
        self.n2.place(x=50,y=100)

        Button(self.ven,text='Validar',command=self.Enviar,width=10,fg='green').place(x=30,y=140)
        Button(self.ven,text='Cerrar',command=self.Cerrar,width=10,fg='red').place(x=150,y=140)

    def Enviar(self):
        u = self.n1.get()
        p = self.n2.get()

        con = sqlite3.connect("Usuarios.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario=? and password=?", (u,p))
        resultado = cursor.fetchone()
        con.close()

        if resultado:
            self.n1.delete(0,END)
            self.n2.delete(0,END)
            self.ven.withdraw()
            otra = Toplevel(self.ven)
            Ventanados(otra,self.ven,u)
        else:
            messagebox.showerror('Error','Datos incorrectos')
            self.n1.delete(0,END)
            self.n2.delete(0,END)

    def Cerrar(self):
        self.ven.destroy()

class Ventanados():
    def __init__(self,master,ven,u):
        self.ven = ven
        self.usuario = u
        self.dos = master
        self.dos.title('Programa 1')

        ancho = 500
        alto = 320
        ventana_ancho = self.dos.winfo_screenwidth()
        ventana_alto = self.dos.winfo_screenheight()
        x = (ventana_ancho // 2) - (ancho // 2)
        y = (ventana_alto // 2) - (alto // 2)
        self.dos.geometry(f'{ancho}x{alto}+{x}+{y}')

        Button(self.dos,text='Regresar',command=self.Regresar,width=10).place(x=150,y=140)

        self.us = Label(self.dos,text=f'Bienvenido \n {self.usuario}')
        self.us.place(x=400,y=1)

        self.Mostrar()
        self.mostrarTabla()

        self.menus = tk.Menu(self.dos)
        self.dos.config(menu=self.menus)

        self.archivos = tk.Menu(self.menus,tearoff=0)
        self.archivos.add_command(label='Agregar',command=self.Crearusuario)
        self.indexAgregar = self.archivos.index("end")
        self.archivos.add_command(label='Modificar',command=self.Modificarus)
        self.indexModificar = self.archivos.index("end")
        self.archivos.add_command(label='Eliminar',command=self.Eliminarusr)
        self.indexEliminar = self.archivos.index("end")
        self.archivos.add_command(label='Salir',command=self.salir)
        self.menus.add_cascade(label='Archivo',menu=self.archivos)

        self.archivos.entryconfig(self.indexAgregar,state = 'disable')
        self.archivos.entryconfig(self.indexEliminar,state = 'disable')
        self.archivos.entryconfig(self.indexModificar,state = 'disable')

        self.roles()
    def roles(self):
        if self.usuario == 'admin':
            self.archivos.entryconfig(self.indexAgregar,state='normal')
            self.archivos.entryconfig(self.indexEliminar,state='normal')
            self.archivos.entryconfig(self.indexModificar,state='normal')

        elif self.usuario == 'Supervisor' or self.usuario == 'supervisor':
            self.archivos.entryconfig(self.indexAgregar,state='normal')
            self.archivos.entryconfig(self.indexEliminar,state='disable')
            self.archivos.entryconfig(self.indexModificar,state='disable')

        elif self.usuario == 'Jefe de area' or self.usuario == 'jefe de area':
            self.archivos.entryconfig(self.indexAgregar,state='disable')
            self.archivos.entryconfig(self.indexEliminar,state='normal')
            self.archivos.entryconfig(self.indexModificar,state='disable')
    # ----------------------------------------------------

    def Crearusuario(self):
        if len(self.usu.get()) != 0 and len(self.pas.get()) != 0:
            con = sqlite3.connect("Usuarios.db")
            cursor = con.cursor()
            cursor.execute("INSERT INTO usuarios (usuario,password) VALUES (?,?)", (self.usu.get(), self.pas.get()))
            con.commit()
            con.close()
            self.Actualizartabla()
            self.borrarcaja('Usuario agregado correctamente')
        else:
            messagebox.showerror('Error','Faltan Datos')

    def Seleccionfila(self, event):
        try:
            index = self.tabla.selection()[0]
        except:
            return
        
        valores = self.tabla.item(index,"values")
        self.usu.delete(0,END)
        self.pas.delete(0,END)
        self.usu.insert(0,valores[1])
        self.pas.insert(0,valores[2]) 
        
    def Actualizartabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        self.mostrarTabla()

    def Modificarus(self):
        try:
            index = self.tabla.selection()[0]
        except:
            messagebox.showerror('Error','Elige un usuario')
            return
        
        valores = self.tabla.item(index,"values")
        id = valores[0]

        if len(self.usu.get()) != 0 and len(self.pas.get()) != 0:
            u = self.usu.get()
            p = self.pas.get()
            con = sqlite3.connect("Usuarios.db")
            cursor = con.cursor()
            cursor.execute("UPDATE usuarios SET usuario=?, password=? WHERE id=?", (u, p, id))
            con.commit()
            con.close()
            self.Actualizartabla()
            self.borrarcaja('Usuario modificado correctamente')
        else:
            messagebox.showerror('Error','Faltan datos')

    def Eliminarusr(self):
        try:
            index = self.tabla.selection()[0]
            valores = self.tabla.item(index,"values")
            id = int(valores[0])
            usuario = valores[1]
            if usuario == self.usuario:
                self.borrarcaja()
                messagebox.showerror('Error','No puedes eliminar tu propio usuario')
            else:
                con = sqlite3.connect("Usuarios.db")
                cursor = con.cursor()
                cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
                cursor.execute("UPDATE usuarios SET id = id - 1 WHERE id > ?", (id,))
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='usuarios'")
                con.commit()
                con.close()
                self.Actualizartabla()
                self.borrarcaja('Usuario borrado correctamente')
        except:
            messagebox.showerror('Error','Elige un usuario')

    def salir(self):
        self.dos.destroy()
        self.ven.destroy()

    def mostrarTabla(self):
        con = sqlite3.connect("Usuarios.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios")
        for i in cursor.fetchall():
            self.tabla.insert("",END,values=i)
        con.close()

    def Mostrar(self):
        columnas = ("ID","USUARIO","PASSWORD")
        self.tabla = ttk.Treeview(self.dos,columns=columnas,show='headings')
        self.tabla.place(x=10,y=100,width=350,height=190)
        for col in columnas:
            self.tabla.heading(col,text=col)
            self.tabla.column(col,anchor='center',width=30)

        scrolly = ttk.Scrollbar(self.dos,orient='vertical',command=self.tabla.yview)
        scrollx = ttk.Scrollbar(self.dos,orient='horizontal',command=self.tabla.xview)
        scrolly.place(x=360,y=90,height=200)
        scrollx.place(x=10,y=280,width=350)

        Label(self.dos,text='Escribe el usuario').place(x=10,y=10)
        self.usu = Entry(self.dos)
        self.usu.place(x=10,y=30)

        Label(self.dos,text='Escribe el password').place(x=150,y=10)
        self.pas = Entry(self.dos)
        self.pas.place(x=150,y=30)
        self.tabla.bind("<<TreeviewSelect>>",self.Seleccionfila)

    def borrarcaja(self,mensaje=''):
        self.usu.delete(0,END)
        self.pas.delete(0,END)
        if mensaje:
            messagebox.showinfo('Listo',mensaje)

    def Regresar(self):
        self.dos.destroy()
        self.ven.deiconify()

if __name__ == '__main__':
    crearBaseDatos()
    master = Tk()
    app = Ventana(master)
    app.Inicio()
    master.mainloop()
