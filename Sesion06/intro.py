import numpy as np

mi_lista_de_temperatura = [20.5, 22.0, 19.5, 21.0, 23.5]

temperaturas = np.array (mi_lista_de_temperaturas)
print(temperaturas)

arreglo3d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]]
)
print(np.mean(arreglo3d, axis=0)) # promedio por columnas
print(np.mean(arreglo3d, axis=1)) # promedio por filas
print(np.mean(arreglo3d)) # promedio por filas
print(arreglo3d [0:2]) #Filas
print(arreglos3d[0:2, 1:3]) # Filas 0 y 1, columnas 1 y 2

print(arreglo3d.shape)
print(arreglo3d.reshape(3,2))
print(len(arreglo3d))
print(arreglo3d.ndim) # Número de dimensiones
print(arreglo3d.dtype) # tipo de dato
print(arreglo3d ! = arreglo3d2)
arreglo3d.resshape(5,1)
print (arreglo3d.flatten ()) # Aplana el arreglo a una dimensión



