#lista
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#primer elemento
print(myFruitList[0])

### cambio mango por melon

myFruitList[2] = "melon"

###metodo de las listas
#.append. agregar elemento a la lista

#añadir tomate a la lista

myFruitList.append("tomate")
print(myFruitList)

#tupla coleccion ordenada de elementos, e inmutable
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])

#diccionario

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)

print(type(myFavoriteFruitDictionary))

### traer fondo de akua

print((myFavoriteFruitDictionary["Akua"]))

#agregar fondo
myFavoriteFruitDictionary["limon"] = "Gris"