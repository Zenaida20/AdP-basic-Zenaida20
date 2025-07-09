
import argparse

def monitorear_caida_presion(v_presion, valor_minimo, delta, mensaje_presion):
    presion = v_presion

    while presion > valor_minimo:
        print(mensaje_presion, presion)
        presion -= delta

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitorea la caída de presión.")
    parser.add_argument("presion_inicial", type=int, help="Presión inicial")
    parser.add_argument("valor_minimo", type=int, help="Valor mínimo de presión")
    parser.add_argument("delta", type=int, help="Decremento de presión en cada iteración")
    parser.add_argument("delta", type=int, help="Decremento de presión en cada iteración")
    parser.add_argument("--mensaje_presion", type=str, default="The current presion is: ", help="Mensaje a mostrar")

    args = parser.parse_args()

    monitorear_caida_presion(args.presion_inicial, args.valor_minimo, args.delta, args.mensaje_presion)