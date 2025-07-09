from validador import verificar_presion

presiones = [99, 100, 150, 200, 250, 300, 301]

for presion in presiones:
    resultado = verificar_presion(presion)
    print(f"Presion: { presion} - {resultado}")

produccion = [100, 200, 300, 400, 500]

total = calcular_volumen_total(produccion)
