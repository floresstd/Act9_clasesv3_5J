print("Act 9 Clases V3") 
print("Jesús Daniel Flores Rodríguez 22308051281186")

class Operadores1186:
    def suma1186(self, J, F):
        s1186 = J + F
        print(f"La suma de {J} + {F} = {s1186}")

    def resta1186(self, J, F):
        r1186 = J - F
        print(f"La resta de {J} - {F} = {r1186}")

    def multiplicacion1186(self, J, F):
        m1186 = J * F
        print(f"La multiplicación de {J} * {F} = {m1186}")

    def division1186(self, J, F):
        if F != 0:
            d1186 = J / F
            print(f"La división de {J} / {F} = {d1186}")
        else:
            print("Error: División entre cero.")

    def modulo1186(self, J, F):
        mod1186 = J % F
        print(f"El módulo de {J} % {F} = {mod1186}")

    def exponente1186(self, J, F):
        exp1186 = J ** F
        print(f"{J} elevado a {F} = {exp1186}")

    def coeficiente1186(self, J, F):
        if F != 0:
            coef1186 = J // F
            print(f"El coeficiente (división entera) de {J} // {F} = {coef1186}")
        else:
            print("Error: División entre cero.")

operadorflores = Operadores1186()

print("Funciones de operaciones:")
operadorflores.suma1186(11, 2)
operadorflores.resta1186(11, 2)
operadorflores.multiplicacion1186(11, 2)
operadorflores.division1186(11, 2)
operadorflores.modulo1186(11, 2)
operadorflores.exponente1186(11, 2)
operadorflores.coeficiente1186(11, 2)
