from typing import List


list = []
num = 0
while num <= 10:
    list.append(num)
    num += 1
print(list)
list.reverse()
print (list)



dictionary = {
    "clave1": "Patata",
    "clave2" : "Manzana",
    "clave3": "Zanahoria",
    "clave4": "Camiseta"
}
for key, value in dictionary.items():
    print(value) 

dictionary["clave2"] = "Valor cambiado"
print(dictionary)

dictionary["Clave5"] = ["Patata","tomate"]
dictionary.update({"Age": [18, 20, 25, 29, 30]})
print(dictionary)

## Este código me da problemas de sintaxis. ¿Puedes responder en los comentarios? ¿Se debe al intérprete de python?
#"message": "Argument of type \"list[str]\" cannot be assigned to parameter \"__value\" of type \"str\" in function \"__setitem__\"\n  \"list[str]\" is incompatible with \"str\"",
