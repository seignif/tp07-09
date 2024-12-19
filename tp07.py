import math


class Fraction:
    def __init__(self, num: int = 0, den: int = 1):
        """
        Initialize a fraction.

        Preconditions:
        - `num` and `den` must be integers.
        - `den` must not be zero.

        Postconditions:
        - The fraction is stored in reduced form.
        - The denominator is always positive.

        Raises:
        - TypeError: if `num` or `den` are not integers or are booleans.
        - ValueError: if `den` is zero.
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
        """
        Get the numerator of the fraction.

        Postconditions:
        - Returns the numerator as an integer.
        """
        return self._numerator

    @property
    def denominator(self) -> int:
        """
        Get the denominator of the fraction.

        Postconditions:
        - Returns the denominator as a positive integer.
        """
        return self._denominator

    def __str__(self) -> str:
        """
        Get the string representation of the fraction.

        Postconditions:
        - Returns a string in the form "numerator/denominator" or "numerator" if the denominator is 1.
        """
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

    def as_mixed_number(self) -> str:
        """
        Convert the fraction to a mixed number string.

        Postconditions:
        - Returns a string in the form "integer and numerator/denominator" or "integer" if no remainder exists.
        """
        integer_part = self._numerator // self._denominator
        remainder = abs(self._numerator % self._denominator)
        if remainder == 0:
            return str(integer_part)
        return f"{integer_part} and {remainder}/{self._denominator}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Add another fraction or an integer to this fraction.

        Preconditions:
        - `other` must be an instance of Fraction or an integer.

        Postconditions:
        - Returns a new Fraction representing the sum.

        Raises:
        - TypeError: if `other` is not a Fraction or an integer.
        """
        if isinstance(other, int):
            return self + Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Can only add two Fraction objects.")
        new_num = self._numerator * other.denominator + other.numerator * self._denominator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Subtract another fraction from this fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns a new Fraction representing the difference.

        Raises:
        - TypeError: if `other` is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract two Fraction objects.")
        new_num = self._numerator * other.denominator - other.numerator * self._denominator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Multiply this fraction by another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns a new Fraction representing the product.

        Raises:
        - TypeError: if `other` is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply two Fraction objects.")
        new_num = self._numerator * other.numerator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """
        Divide this fraction by another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.
        - `other`'s numerator must not be zero.

        Postconditions:
        - Returns a new Fraction representing the quotient.

        Raises:
        - TypeError: if `other` is not a Fraction.
        - ZeroDivisionError: if `other`'s numerator is zero.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide two Fraction objects.")
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with numerator zero.")
        new_num = self._numerator * other.denominator
        new_den = self._denominator * other.numerator
        return Fraction(new_num, new_den)

    def __pow__(self, power: int) -> 'Fraction':
        """
        Raise this fraction to the power of an integer.

        Preconditions:
        - `power` must be an integer.

        Postconditions:
        - Returns a new Fraction representing the result.

        Raises:
        - TypeError: if `power` is not an integer.
        """
        if not isinstance(power, int):
            raise TypeError("Power must be an integer.")
        if power >= 0:
            return Fraction(self._numerator ** power, self._denominator ** power)
        else:
            return Fraction(self._denominator ** abs(power), self._numerator ** abs(power))

    def __eq__(self, other: 'Fraction') -> bool:
        """
        Check if this fraction is equal to another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns True if the fractions are equal, False otherwise.
        """
        if not isinstance(other, Fraction):
            return False
        return self._numerator == other.numerator and self._denominator == other.denominator

    def __ne__(self, other: 'Fraction') -> bool:
        """
        Check if this fraction is not equal to another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns True if the fractions are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other: 'Fraction') -> bool:
        """
        Check if this fraction is less than another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns True if this fraction is less than `other`, False otherwise.

        Raises:
        - TypeError: if `other` is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare two Fraction objects.")
        return self._numerator * other.denominator < other.numerator * self._denominator

    def __le__(self, other: 'Fraction') -> bool:
        """
        Check if this fraction is less than or equal to another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns True if this fraction is less than or equal to `other`, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: 'Fraction') -> bool:
        """
        Check if this fraction is greater than another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns True if this fraction is greater than `other`, False otherwise.

        Raises:
        - TypeError: if `other` is not a Fraction.
        """
        return not self.__le__(other)

    def __ge__(self, other: 'Fraction') -> bool:
        """
        Check if this fraction is greater than or equal to another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns True if this fraction is greater than or equal to `other`, False otherwise.
        """
        return self.__eq__(other) or self.__gt__(other)

    def __float__(self) -> float:
        """
        Convert this fraction to a float.

        Postconditions:
        - Returns the float representation of the fraction.
        """
        return self._numerator / self._denominator

    def __abs__(self) -> 'Fraction':
        """
        Get the absolute value of this fraction.

        Postconditions:
        - Returns a new Fraction representing the absolute value of this fraction.
        """
        return Fraction(abs(self._numerator), self._denominator)

    def is_zero(self) -> bool:
        """
        Check if this fraction is zero.

        Postconditions:
        - Returns True if the numerator is 0, False otherwise.
        """
        return self._numerator == 0

    def is_integer(self) -> bool:
        """
        Check if this fraction is an integer.

        Postconditions:
        - Returns True if the fraction represents an integer, False otherwise.
        """
        return self._numerator % self._denominator == 0

    def is_proper(self) -> bool:
        """
        Check if this fraction is a proper fraction.

        Postconditions:
        - Returns True if the absolute value of the numerator is less than the denominator, False otherwise.
        """
        return abs(self._numerator) < self._denominator

    def is_unit(self) -> bool:
        """
        Check if this fraction is a unit fraction.

        Postconditions:
        - Returns True if the absolute value of the numerator is 1, False otherwise.
        """
        return abs(self._numerator) == 1

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """
        Check if this fraction is adjacent to another fraction.

        Preconditions:
        - `other` must be an instance of Fraction.

        Postconditions:
        - Returns True if the difference between this fraction and `other` is a unit fraction, False otherwise.

        Raises:
        - TypeError: if `other` is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only check adjacency with another Fraction object.")
        difference = abs(self - other)
        return difference.numerator == 1 and difference.denominator > 0

    def as_decimal(self) -> float:
        """
        Get the decimal representation of this fraction.

        Postconditions:
        - Returns the decimal value of the fraction as a float.
        """
        return self._numerator / self._denominator
