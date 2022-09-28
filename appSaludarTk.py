# Crear pequeña app de escritorio para saludar usuarios, generando lista de 5 elementos, e imprimiendo mensajes de error en caso
# de ingresar cadena vacía o superar el número de saludos

import tkinter as tk
from tkinter import ttk, messagebox

def saludar():
    global saludos
    salida.delete(0, tk.END)
    nombre = entrada.get()
    
    if saludos < 5:

        if nombre == "" or nombre == " ":
            messagebox.showerror(title="Error", message = "Es de locos andar saludando al vacío")
            
        else:
            salida.insert(0,  f"<<             ¡Hola {nombre}!             >>" )
            lista.insert(0, "=>  " + nombre)
            saludos +=1

    else:
        messagebox.showerror(title="Demasiados", message = "No hay que abusar de la simpatía")
        ventana_ppal.destroy()
        
    
saludos = 0

ventana_ppal = tk.Tk()
ventana_ppal.title("Programa clase 3")
ventana_ppal.config(width=300, height=340)

entrada = ttk.Entry()
entrada.place(x=20, y=30, width=170, height=25 )

boton = ttk.Button(text="¡Saludar!", command=saludar)
boton.place(x=200, y=30, width=80,  height=25)

salida = ttk.Entry()
salida.place(x=20, y=90, width=260, height=120)

lista = tk.Listbox()
lista.place(x=20, y=220, width=260, height=90)


ventana_ppal.mainloop()