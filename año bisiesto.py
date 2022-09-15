from operator import truediv


def abisiesto(year):
    if year%4 == 0: 
        return print("El año es bisiesto")
    else:
        return print("El año no es bisiesto")

abisiesto(2024)