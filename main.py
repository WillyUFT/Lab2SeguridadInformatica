# Vamos a hacer una interfaz para que se vea lindo, importemos tkinter
import tkinter as TK
from tkinter import messagebox as msg
from turtle import color, title  # Biblioteca para realizar interfaces gráficas
import cifrados
import leerTxt as txt

# Mensaje Hasheado original
mensajeHasheadoOriginal = ""

# Acá están las acciones que cada botón debe ejecutar
def AccionesBotones(boton):
    global mensajeHasheadoOriginal
    # Acá entramos para leer el txt de entrada
    if boton == "leerTxtEntrada":
        # Se toma el mensaje que está escrito en el txt de entrada
        msjEntrada = txt.leerTexto("mensajedeentrada.txt")
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensaje.delete("1.0", "end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensaje.insert("end", msjEntrada)

    # Acá entramos para hacer el hash al mensaje cifrado o no
    elif boton == "hacerHash":
        # Acá tomamos el mensaje que sacamos del txt y lo mandamos a la función del hash
        msjHasheado = cifrados.hash(mensajeEncriptado.get(1.0, "end-1c"))
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensajeEncriptado.delete("1.0", "end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensajeEncriptado.insert("end", "Mensaje Hasheado: \n" + str(msjHasheado))
        # Se guarda el mensaje hasheado original para compararlo con el txt de salida
        mensajeHasheadoOriginal = msjHasheado
        # Se escribe el mensaje hasheado en el txt de salida
        txt.escribirTextoSalida(msjHasheado)

    # Acá entramos para hacer los cifrados
    elif boton == "cifradoCompleto":
        # Se toma el mensaje escrito en la casilla de mensaje
        msjCifrado = cifrados.redCifrado(mensaje.get(1.0, "end-1c"), "pekopeko")
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensajeEncriptado.delete("1.0", "end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensajeEncriptado.insert("end", "Mensaje cifrado: " + msjCifrado)

    # Acá entramos para comprobar la integridad del mensaje
    elif boton == "ComprobarMensaje":
        # Leemos el txt de salida
        msjTextoSalida = txt.leerTexto("mensajeseguro.txt")
        # Si el mensaje que está en el txt de salida es 
        # igual al mensaje hashado que habíamos guardado antes
        if msjTextoSalida == mensajeHasheadoOriginal:
            # Mostramos un mensaje para decir que el mensaje está bien
            msg.showinfo(
                title="Información", message="El mensaje no ha sido modificado"
            )
        # En caso de que hayan discordancias entre los mensajes
        else:
            # se envía un mensaje para avisar que el mensaje ha sido modificado.
            msg.showerror(title="Información", message="El mensaje ha sido modificado")


# Creamos la ventana
ventana = TK.Tk()
ventana.geometry("1000x500")
ventana.resizable(height=False, width=False)
ventana.title("Seguridad informática")
ventana.iconbitmap("miko.ico")

# Fondito
pantalla = TK.PhotoImage(file="akukin.png")
fotopantalla = TK.Label(ventana, image=pantalla)
fotopantalla.place(x=0, y=0)


# Lado izquierdo de Aqua
# Este es el cosito que dice mensaje
mensajeLabel = TK.Label(ventana, text="Mensaje")
mensajeLabel.place(x=100, y=170, width=190)

# Acá se pondrá el mensaje que quiere encriptar el cliente.
mensaje = TK.Text(ventana)
mensaje.place(x=100, y=190, width=190, height=100)

# Este es el cosito que dice encriptar y eso
botonesEncriptadoLabel = TK.Label(ventana, text="Encriptar mediante: ")
botonesEncriptadoLabel.place(x=100, y=330, width=190)

# Boton para leer el archivo txt
TK.Button(
    ventana, text="Leer archivo .txt", command=lambda: AccionesBotones("leerTxtEntrada")
).place(x=100, y=300, width=190)

# Lado derecho de Aqua
# Este es el cosito que dice mensaje encriptado
mensajeEncriptadoLabel = TK.Label(ventana, text="Mensaje encriptado")
mensajeEncriptadoLabel.place(x=710, y=170, width=190)

# Acá se pondrá el mensaje que quiere encriptar el cliente.
mensajeEncriptado = TK.Text(ventana)
# mensajeEncriptado.config(state=TK.DISABLED)
mensajeEncriptado.place(x=710, y=190, width=190, height=100)

# Este es el cosito que dice encriptar y eso
botonesDesEncriptadoLabel = TK.Label(ventana, text="Desencriptar mediante: ")
botonesDesEncriptadoLabel.place(x=710, y=300, width=190)

# Boton para el desafío 1
TK.Button(
    ventana,
    text="Cifrado con la red completa",
    command=lambda: AccionesBotones("cifradoCompleto"),
).place(x=100, y=355, width=190)

# Boton para hacer el hash
TK.Button(
    ventana, text="Aplicar Hash", command=lambda: AccionesBotones("hacerHash")
).place(x=710, y=325, width=190)

# Boton para verificar si el mensaje no ha sido modificado
TK.Button(
    ventana,
    text="Comprobar mensaje",
    command=lambda: AccionesBotones("ComprobarMensaje"),
).place(x=710, y=355, width=190)


# Coso para que no se cierre
ventana.mainloop()
