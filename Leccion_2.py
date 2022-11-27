def operaciones(num1: int, num2: int):
    try:
        suma = num1 + num2
        resta = num1 - num2
    except Exception as e:
        print(f'Ha habido un error de tipo {e}')
    else:
         return suma, resta
    # finally:
    #     print('Operación realizada')  
print(operaciones(5,7))
print(operaciones('2', 5))



#Crea una función en la cual el segundo parámetro sea un argumento predeterminado.
number = input('Introduce un número al que quieras sumar')
number = int(number)
def sumar4 (num1, num2=4):
    resul = num1 + num2
    return print(resul)
sumar4(number)
