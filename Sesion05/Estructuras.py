inventario = ["abel", "Abel", "Gasolina"]
inventario= ["Crudo", "Gas Natural", "Gasolina"]

#Agregra un elemento al final de la lista
inventario.append("Carbon")    
inventario.append("Gas Licuado")
inventario.append("Diesel")

#Adicional un elemento en la segunda posición de la lista
inventario.insert(1, "Hidrogeno")

#Ordenar de la A a la Z
inventario.sort
print(inventario)

#Ordenar de la A a la Z
inventario.sort(reverse=True)
print(inventario)
