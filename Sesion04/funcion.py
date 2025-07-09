

celsius_input = float (input (Introduce la tem

print(conversion_grados_celsius_a_farenhedef conversion_grados_celsius_a_farenheith(celsius):

    if not isinstance(celsius, (int, float))
    raise ValueError ("La Temperatura debe ser un número")

farenheith = celsius * 9/5 + 32
return farenheithith(celsius_input))

 def conversion_grados_farenheith_a_celsius(farenheith):

    if not isinstance(farenheith, (int, float)):
    raise ValueError ("La Temperatura debe ser un número")

    celsius = (farenheith - 32) * 5/9
    return conversion_grados_celsius_a_farenheith

farenheith_input = float(input("Introduce la temperatura en grados Farenheith"))

print(conversion_grados_farenheith_a_celsius(farenheith_input))

