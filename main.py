from tp07 import Fraction

try:
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print(f"Addition: {f1} + {f2} = {f1 + f2}")
    print(f"Multiplication: {f1} * {f2} = {f1 * f2}")
    print(f"Division: {f1} / {f2} = {f1 / f2}")
    print(f"As mixed number: {f2.as_mixed_number()}")
    print(f"Is integer: {f1.is_integer()}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
