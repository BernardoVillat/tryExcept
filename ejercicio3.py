class ValidadorContraseña:
    def validar(self, contraseña, longitud_minima):
        if len(contraseña) < longitud_minima:
            raise ValueError(f"La contraseña no cumple con la longitud mínima de {longitud_minima} caracteres")
        print("La contraseña ha sido guardada exitosamente")

validador = ValidadorContraseña()
try:
    contraseña = input("Ingrese una contraseña: ")
    longitud_minima = 8
    validador.validar(contraseña, longitud_minima)
except ValueError as e:
    print(e)




