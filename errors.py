try:
    print(0/0)
    assert 1 != 1, 'Uno es igual a uno'
    age = 10
    if age < 18:
        raise Exception("No es mayor de edad")

except ZeroDivisionError:
    print("No se puede dividir por cero")
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
else:
    print("No se ha generado ninguna excepcion")