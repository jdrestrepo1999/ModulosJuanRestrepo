# Cuenta la cantidad de palabras en una cadena de texto
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)


# Cuenta la cantidad de veces que esta cada palabra en una cadena de texto
def palabra_frecuencia(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia


# Reemplaza una palabra por otra en una cadena de texto
def remplaza_palabra(texto, palabra_vieja, palabra_nueva):
    return texto.replace(palabra_vieja, palabra_nueva)
