# Devuelve el área de un círculo dado su radio
def area_circulo(radio):
    try:
        if radio < 0:
            return "Error: El radio no puede ser negativo."
        return 3.1416 * radio ** 2
    except TypeError:
        return "Error: El radio debe ser un número."


# Devuelve el perímetro de un círculo dado su radio
def perimetro_circulo(radio):
    try:
        if radio < 0:
            return "Error: El radio no puede ser negativo."
        return 2 * 3.1416 * radio
    except TypeError:
        return "Error: El radio debe ser un número."


# Devuelve el área de un rectángulo dada su base y altura
def area_rectangulo(base, altura):
    try:
        if base < 0 or altura < 0:
            return "Error: La base y la altura no pueden ser negativas."
        return base * altura
    except TypeError:
        return "Error: La base y la altura deben ser números."


# Devuelve el perímetro de un rectángulo dada su base y altura
def perimetro_rectangulo(base, altura):
    try:
        if base < 0 or altura < 0:
            return "Error: La base y la altura no pueden ser negativas."
        return 2 * (base + altura)
    except TypeError:
        return "Error: La base y la altura deben ser números."
