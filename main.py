from tp07 import Fraction

def main():
    try:
        # Création de fractions
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)

        # Opérations de base
        print(f"Addition: {f1} + {f2} = {f1 + f2}")
        print(f"Soustraction: {f1} - {f2} = {f1 - f2}")
        print(f"Multiplication: {f1} * {f2} = {f1 * f2}")
        print(f"Division: {f1} / {f2} = {f1 / f2}")

        # Vérifications des propriétés
        print(f"Fraction {f1} en nombre mixte: {f1.as_mixed_number()}")
        print(f"Fraction {f1} est un entier: {f1.is_integer()}")
        print(f"Fraction {f2} est propre: {f2.is_proper()}")
        print(f"Fraction {f1} est zéro: {f1.is_zero()}")

        # Autres fonctionnalités
        print(f"Valeur absolue de {f1}: {abs(f1)}")
        print(f"Fraction {f2} au carré: {f2 ** 2}")
        print(f"Fraction inversée de {f2}: {f2 ** -1}")
        print(f"Valeur décimale de {f1}: {f1.as_decimal()}")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Erreur: {e}")
    except TypeError as e:
        print(f"Type d'erreur: {e}")

if __name__ == "__main__":
    main()
