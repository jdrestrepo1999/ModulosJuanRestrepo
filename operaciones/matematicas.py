# Devuelve la suma de dos números
def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Ambos parámetros deben ser números"


# Devuelve la resta de dos números
def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Ambos parámetros deben ser números"


# Devuelve la multiplicacion de dos números
def multiplicacion(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Ambos parámetros deben ser números"


# Devuelve la division de dos números
def division(a, b):
    try:
        if b == 0:
            return "Error: División por cero no es permitida"
        return a / b
    except TypeError:
        return "Error: Ambos parámetros deben ser números"
