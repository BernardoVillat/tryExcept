class ValidadorDeEdad:
    def validar(self, edad):
        if edad < 0:
            raise ValueError(f"La edad ingresada: {edad} no es un número entero")
        print("Felicidades, ingresaste una edad válida!! :)")

validador = ValidadorDeEdad()
try:
    edad = int(input("Por favor, ingresa tu edad: "))
    validador.validar(edad)
except ValueError as e:
    print(e)





