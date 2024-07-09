import operaciones.matematicas as mat
import operaciones.geometria as geo
import analisis_texto.operaciones as ant

# Probando libreria "operaciones"
print(mat.multiplicacion(10, 5))
print(mat.division(10, 5))
print(geo.area_rectangulo(10, 5))
print(geo.perimetro_rectangulo(10, 5))
print()
# Probando libreria "analisis_texto"
texto = "Mi nombre es Juan Diego y este es mi trabajo sobre modulos"
print(texto)
print("Cantidad de palabras en texto brindado: ", ant.contar_palabras(texto))
print("Frecuencia de palabras:", ant.palabra_frecuencia(texto))
print("Reemplazamos 'Diego' por 'David':", ant.remplaza_palabra(texto, 'Diego', 'David'))
