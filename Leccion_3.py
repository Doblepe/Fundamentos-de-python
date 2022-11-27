class calculadora:

    #atributos de instancia
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
   
    def sumar (self):
        print(f" Para sumar || El n1 es {self.num1} y el n2 es {self.num2} y el resultado es: ")
        return self.num1 + self.num2
    def restar(self) -> int:
        print(f"Para restar || El n1 es {self.num1} y el n2 es {self.num2} y el resultado es: ")
        return self.num1 - self.num2
    def multiplicar(self) -> int:
        print(f"Para multiplicar || El n1 es {self.num1} y el n2 es {self.num2} y el resultado es: ")
        return self.num1 * self.num2
    def dividir (self) -> int:
        print(f"Para dividir || El n1 es {self.num1} y el n2 es {self.num2} y el resultado es: ")
        return self.num1 / self.num2

calc1 = calculadora(1,6)
calc2 = calculadora(7,9)
calc3 = calculadora(11,22)

# calc2.sumar()
# print(calc3.sumar())
print(calc3.restar())
