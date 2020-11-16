from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



#------------------------------------------------------------------------#

def salir(root):
    root.destroy()
    
def SillasCine():
    root2 = Toplevel()
    root2.title('Consultando')
    root2.geometry("350x200")  # X-Y

    archivo = open("CAIPA1143140121-01S.txt", "r")
    sillas = {}
    
    for linea in archivo:
        
        datos = linea.strip()
        datos = datos.split(":")

        fila = datos[0]
        
        datos = datos[1].split("-")
        columnas = []

        for columna in datos:
            columnas.append(columna)

        if sillas == {}:
            sillas = {fila:columnas}
        else:
            sillas[fila]=columnas
        
        #horas.append(dato[3])
   
    print(sillas)    
    
    archivo.close()

    def salir():
        root2.destroy()

    

    sala = ttk.Label(root2, text="Sala:")
    salacb = ttk.Combobox(root2, width=20, state="readonly")
    salacb['values'] = ('Sala 1', 'Sala 2', 'Sala 3', 'Sala 4')
    sala.grid(row=0, column=0, padx=30, pady=10)
    salacb.grid(row=0, column=1, padx=30, pady=10)

    filasLb = ttk.Label(root2, text="Fila:")
    filasLb.grid(row=1, column=0)
    filasEn = ttk.Combobox(root2, width=20, state="readonly")
    filasEn.grid(row=1, column=1, padx=50, pady=0)
    
    columnaLb = ttk.Label(root2, text="Columna")
    columnaLb.grid(row=2, column=0)
    columnaEn = ttk.Combobox(root2, width=20, state="readonly")
    columnaEn.grid(row=2, column=1, padx=30, pady=10)

    enviarS = ttk.Button(root2, text="Enviar")
    enviarS.grid(row=5, column=0, padx=30, pady=10)
    enviarS = ttk.Button(root2, text="Volver", command=salir)
    enviarS.grid(row=5, column=1, padx=30, pady=10)


#------------------------------------------------------#

  
#-------------------------------INTERFACEZ 2---------------------------------#

def mostrar():
    root = Tk()
    root.title("CINE")

    archivo = open("CAIPA1143140121-01E.txt", "r")
    nom = []
    fech = []
    horas = []
    
    for i in archivo:
        dato = i.split("--")
        nom.append(dato[0])
        fech.append(dato[1])
        horas.append(dato[3])
   
    print(nom)    
    print(fech)
    print(horas)
    archivo.close()


#---------------------------LABELS-------------------------------------#
    nombre = ttk.Label(root, text="Nombre:")
    pelicula = ttk.Label(root, text="Peliculas disponibles:")
    fecha = ttk.Label(root, text="Fecha:")
    formato = ttk.Label(root, text="Formato:")
    hora = ttk.Label(root, text="Hora de funcion:")

    pelicula.grid(row=1, column=0, padx=20, pady=10)
    fecha.grid(row=2, column=0, padx=20, pady=10)
    formato.grid(row=3, column=0, padx=20, pady=10)
    hora.grid(row=5, column=0, padx=20, pady=10)

#-------CMBX----------------------------------------------------------#
    
    peliculatxt = ttk.Combobox(root, width=20, state="readonly")#----------
    peliculatxt['values'] = nom
    peliculatxt.grid(row=1, column=1, padx=20, pady=10)
    
    fechatxt = ttk.Combobox(root, width=20, state="readonly")#---------
    fechatxt['values'] = fech
    fechatxt.grid(row=2, column=1, padx=20, pady=10)
    
    formatocb = ttk.Combobox(root, width=20, state="readonly")#---------
    formatocb['values'] = ('2D', '3D')
    formatocb.grid(row=3, column=1, padx=20, pady=10)
    
    horacb = ttk.Combobox(root, width=20, state="readonly")
    horacb['values'] = ('2:00 PM', '4:00 PM', '7:00 PM', '10:00 PM')#--------
    horacb.grid(row=5, column=1, padx=20, pady=10)
    


    #-------------------Button-----------#
    enviar = ttk.Button(root, text="Enviar")
    sillas = ttk.Button(root, text="Asignar sillas", command=SillasCine)

    enviar.grid(row=9, column=1, padx=10, pady=10)
    sillas.grid(row=8, column=1, padx=10, pady=10)

    #acerca = ttk.Button(root, text="Acerca De", command = acercaDe)
    cancelar = ttk.Button(root, text="Salir", command =lambda : salir(root))

    #acerca.grid(row=8, column=0, padx=10, pady=10)
    cancelar.grid(row=9, column=0, padx=10, pady=10)


    root.mainloop()



#---------------------------------------------------------------------------/


#-----------------------------------mainframe-----------------------------------------#

main = Tk()
main.title("CINE")
mainframe = ttk.Frame(main)
lbl = ttk.Label(mainframe, text="CINE.TK", background="red", font=("Arial Bold", 30))
btn_fun = ttk.Button(mainframe, text="PELICULAS EN CARTELERA5", command=mostrar )
#btn_taq = ttk.Button(mainframe, text="TAQUILLA")
#------------------info--------------------#
info = """Nombre Completo    Josue Caipa Bolivar
Numero Cedula         1143140121
Fecha Nacimiento      09-06.1993
Correo Personal         yosuecaipa@gmail.com"""
#-----------------------------------------#
btn_info = ttk.Button(mainframe,text="Acerca de ...",command=lambda:messagebox.showinfo("Acerca de ...", info))

lbl.grid(row=0, column=0, padx=30, pady=10)
btn_fun.grid(row=1, column=0, padx=30, pady=10)
#btn_taq.grid(row=2, column=0, padx=30, pady=10)
btn_info.grid(row=3, column=0, padx=30, pady=10)

mainframe.grid(row=0, column=0, padx=10, pady=10)

main.mainloop()
