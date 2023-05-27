import math

def quadratic_equation_solver(a, b, c):
    # Berechne die Diskriminante
    discriminant = b**2 - 4*a*c

    # Überprüfe die Anzahl der Lösungen
    if discriminant > 0:
        # Zwei reelle Lösungen
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # Eine doppelte Lösung
        x = -b / (2*a)
        return x
    else:
        # Keine reelle Lösung
        return None

# Benutzereingabe
a = float(input("Geben Sie den Wert für a ein: "))
b = float(input("Geben Sie den Wert für b ein: "))
c = float(input("Geben Sie den Wert für c ein: "))

# Löse die quadratische Gleichung
solution = quadratic_equation_solver(a, b, c)

# Ausgabe der Lösungen
if solution is None:
    print("Die quadratische Gleichung hat keine reelle Lösung.")
elif isinstance(solution, tuple):
    print("Die quadratische Gleichung hat zwei Lösungen:")
    print("x1 =", solution[0])
    print("x2 =", solution[1])
else:
    print("Die quadratische Gleichung hat eine doppelte Lösung:")
    print("x =", solution)

