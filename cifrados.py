# Cifrado rot
def rotN(mensaje, n):
    # String mensaje
    mensajeCifrado = ""
    # En caso de que el rot indicado sea menor a 0
    if n < 0:
        n = 26 + n
    # Se recorren todos los caracteres del mensaje
    # También se deja todo el mensaje en mayúsculas
    for caracter in mensaje.upper():
        # Si el caracter es alfabético (a-z)
        if caracter.isalpha():
            # Se toma el caracter y se transforma a unicode con ord(), se le resta 65 y se le suma el n
            caracerInt = ord(caracter) - 65 + n
            # Si el caracter en unicode es mayor o igual a 26 se saca el módulo con 26 (abecedario)
            if caracerInt >= 26:
                caracerInt = caracerInt % 26
            # Ahora el unicode que obtuvimos lo cambiamos nuevamente a caracter con chr()
            caracter = chr(caracerInt + 65)
        # Agregamos el caracter al string mensaje para después mostrarlo
        mensajeCifrado += caracter
    return mensajeCifrado


# Esta es la tabla de cifrado vignere que está en el git
tabla = {}
abc = [chr(i) for i in range(65, 65 + 26)] * 2
columnas = abc[:26]
for i in range(26):
    llaveFila = abc[i]
    valoresFila = abc[i: i + 26]
    # Se crea un diccionario gigante que contiene toda la tabla de la forma A:{A:A,B:B} , etc.
    tabla[llaveFila] = dict(zip(columnas, valoresFila))

# Cifrado Vignere


def vigenere(mensaje, llave):
    # String del mensaje
    mensajeCifrado = ""
    contador = 0
    # Este while es para que en caso de que la llave sea de menor longitud que el mensaje
    # Se escriba nuevamente hasta que sea de igual o mayor longitud
    while len(llave) < len(mensaje):
        llave += llave
    # Se recorren todos los caracteres del mensaje
    # También se deja todo el mensaje en mayúsculas
    for caracter in mensaje.upper():
        # Si el caracter no es alfabético, lo agregamos al string del mensaje
        if not caracter.isalpha():
            mensajeCifrado += caracter
        # En caso contrario
        else:
            # Va tomando letra por letra la clave, en mayúsculas
            fila = llave[contador].upper()
            # Busca en la tabla la letra correspondiente y la agrega al mensaje
            mensajeCifrado += tabla[fila][caracter]
            # contador +1
            contador += 1
    return mensajeCifrado

# Descifrado Vignere


def des_vigenere(mensajeCifrado, llave):
    # String del mensaje
    mensajeDescifrado = ""
    contador = 0
    # Este while es para que en caso de que la llave sea de menor longitud que el mensaje
    # Se escriba nuevamente hasta que sea de igual o mayor longitud
    while len(llave) < len(mensajeCifrado):
        llave += llave
    # Se recorren todos los caracteres del mensaje
    # También se deja todo el mensaje en mayúsculas
    for caracter in mensajeCifrado.upper():
        # Si el caracter no es alfabético, lo agregamos al string del mensaje
        if not caracter.isalpha():
            mensajeDescifrado += caracter
        # En caso contrario
        else:
            # Va tomando letra por letra la clave, en mayúsculas
            fila = llave[contador].upper()
            dictFila = tabla[fila]
            # llaves y valores de la fila diccionario de la tabla
            llaves = dictFila.keys()
            valores = dictFila.values()
            # zip empareja en tuplas, elementos con la misma posicion
            # se forma diccionario inverso, ya que se busca el caracter
            # del mensajeDescifrado original, lo que se encuentra como llave del
            # diccionario original
            dictFilaInverso = dict(zip(valores, llaves))
            # Busca en la tabla la letra correspondiente y la agrega al mensaje
            mensajeDescifrado += dictFilaInverso[caracter]
            # contador +1
            contador += 1
    return mensajeDescifrado

# Función para el desafío 1


def redCifrado(mensaje, password):
    # Primero ciframos el mensaje con el rot 8
    mensajeCifrado = rotN(mensaje, 8)
    # Luego por vignere con la contraseña heropassword
    mensajeCifrado = vigenere(mensajeCifrado, password)
    print(mensajeCifrado)
    return mensajeCifrado
