# Cálculo de Temperatura de Celsius a Fahrenheit: Esto es por lista

# Mi Lista de temperaturas en Celsius
celsius = [15, 20, 305, 405]

# El convertidor de Celsius a Fahrenheit
fahrenheit = [temp * 9/5 + 32 for temp in celsius]

# Mostrar resultados
print("Resultado de Temperaturas en Fahrenheit:", fahrenheit)

# Cálculo de Temperatura de Celsius a Fahrenheit: Esto es por Arreglos

# Mi Lista de temperaturas en Celsius
celsius = [15, 20, 305, 405]

# El convertidor de Celsius a Fahrenheit por array
fahrenheit_array = np.array(celsius * 9/5 + 32)

# Mostrar resultados
print(fahrenheit_array)

#Lista que vaya de 0 hasta 5000 dividido en 50 partes 

# Crear una lista de 50 valores entre 0 y 5000
valores = np.linspace(0, 5000, 50)

print(valores)

