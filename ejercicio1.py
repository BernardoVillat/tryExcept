class Divisor:
    def dividir(self, numerador, denominador):
        try:
            resultado = numerador / denominador
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir por cero."

# Uso de la clase Divisor
calculadora = Divisor()

numerador = int(input("Por favor, ingrese el valor del numerador: "))
denominador = int(input("Por favor, ingrese el valor del denominador: "))

resultado = calculadora.dividir(numerador, denominador)

print(f"Resultado de la división: {resultado}")