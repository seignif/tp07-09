import math

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE: den != 0, num and den are integers and not boolean.
        POST: The fraction is reduced to its simplest form.
        RAISES: ValueError if the denominator is zero, TypeError if inputs are not integers or are booleans.
        """
        if not isinstance(num, int) or not isinstance(den, int) or isinstance(num, bool) or isinstance(den, bool):
            raise TypeError("Numerator and denominator must be integers and not boolean.")
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = math.gcd(num, den)
        self._numerator = num // gcd * (-1 if den < 0 else 1)
        self._denominator = abs(den // gcd)

    @property
    def numerator(self) -> int:
        """Return the numerator of the fraction.

        POST: Returns the numerator of the fraction.
        """
        return self._numerator

    @property
    def denominator(self) -> int:
        """Return the denominator of the fraction.

        POST: Returns the denominator of the fraction.
        """
        return self._denominator

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction.

        POST: Returns a string in the format 'numerator/denominator' or 'numerator' if the denominator is 1.
        """
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

    def as_mixed_number(self) -> str:
        """Return a textual representation of the reduced form of the fraction as a mixed number.

        POST: Returns a string representing the fraction as a mixed number (integer and fraction).
        """
        integer_part = self._numerator // self._denominator
        remainder = abs(self._numerator % self._denominator)
        if remainder == 0:
            return str(integer_part)
        return f"{integer_part} and {remainder}/{self._denominator}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the + operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns a new Fraction which is the result of the addition.
        RAISES: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only add two Fraction objects.")
        new_num = self._numerator * other.denominator + other.numerator * self._denominator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the - operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns a new Fraction which is the result of the subtraction.
        RAISES: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract two Fraction objects.")
        new_num = self._numerator * other.denominator - other.numerator * self._denominator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the * operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns a new Fraction which is the result of the multiplication.
        RAISES: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply two Fraction objects.")
        new_num = self._numerator * other.numerator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the / operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns a new Fraction which is the result of the division.
        RAISES: TypeError if other is not a Fraction.
                ZeroDivisionError if the numerator of the other fraction is zero.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide two Fraction objects.")
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with numerator zero.")
        new_num = self._numerator * other.denominator
        new_den = self._denominator * other.numerator
        return Fraction(new_num, new_den)

    def __pow__(self, power: int) -> 'Fraction':
        """Overloading of the ** operator for fractions.

        PRE: power is an integer.
        POST: Returns a new Fraction raised to the power of 'power'.
        RAISES: TypeError if power is not an integer.
        """
        if not isinstance(power, int):
            raise TypeError("Power must be an integer.")
        if power >= 0:
            return Fraction(self._numerator ** power, self._denominator ** power)
        else:
            return Fraction(self._denominator ** abs(power), self._numerator ** abs(power))

    def __eq__(self, other: 'Fraction') -> bool:
        """Overloading of the == operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns True if the fractions are equal, otherwise False.
        RAISES: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            return False
        return self._numerator == other.numerator and self._denominator == other.denominator

    def __ne__(self, other: 'Fraction') -> bool:
        """Overloading of the != operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns True if the fractions are not equal, otherwise False.
        """
        return not self.__eq__(other)

    def __lt__(self, other: 'Fraction') -> bool:
        """Overloading of the < operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns True if the current fraction is less than the other fraction, otherwise False.
        RAISES: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare two Fraction objects.")
        return self._numerator * other.denominator < other.numerator * self._denominator

    def __le__(self, other: 'Fraction') -> bool:
        """Overloading of the <= operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns True if the current fraction is less than or equal to the other fraction.
        """
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: 'Fraction') -> bool:
        """Overloading of the > operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns True if the current fraction is greater than the other fraction.
        """
        return not self.__le__(other)

    def __ge__(self, other: 'Fraction') -> bool:
        """Overloading of the >= operator for fractions.

        PRE: other is an instance of Fraction.
        POST: Returns True if the current fraction is greater than or equal to the other fraction.
        """
        return not self.__lt__(other)

    def __float__(self) -> float:
        """Returns the decimal value of the fraction.

        POST: Returns the floating-point value of the fraction.
        """
        return self._numerator / self._denominator

    def __abs__(self) -> 'Fraction':
        """Returns the absolute value of the fraction.

        POST: Returns a new Fraction that is the absolute value of the current fraction.
        """
        return Fraction(abs(self._numerator), self._denominator)

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0.

        POST: Returns True if the fraction is 0, otherwise False.
        """
        return self._numerator == 0

    def is_integer(self) -> bool:
        """Check if a fraction is an integer.

        POST: Returns True if the fraction is an integer, otherwise False.
        """
        return self._numerator % self._denominator == 0

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1.

        POST: Returns True if the fraction is a proper fraction, otherwise False.
        """
        return abs(self._numerator) < self._denominator

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form.

        POST: Returns True if the fraction is a unit fraction, otherwise False.
        """
        return abs(self._numerator) == 1

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """Check if two fractions differ by a unit fraction.

        PRE: other is an instance of Fraction.
        POST: Returns True if the fractions differ by a unit fraction, otherwise False.
        RAISES: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only check adjacency with another Fraction object.")
        difference = abs(self - other)
        return difference.numerator == 1 and difference.denominator > 0


