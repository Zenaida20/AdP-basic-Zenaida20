# función que valida si la presión se encuentra en un rango

def verificar_presion(presion):
    
    if 100 <= presion <= 300:
        return "presion en rango seguro"
    else:
        return "presion en rango peligroso"
# calcular el volumen total de produccion y devolver el resultado 


def calcular_volumen_total(produccion):
    volumen_total = 0

    if (verificar_presion(produccion) == "presion en rango seguro")
        #suma del valor al volumen total
        volumen_total = volumen_total + produccion
    
    return volumen_total

