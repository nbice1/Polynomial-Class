# Polynomial-Class
Python class for working with polynomials.

Instances of this class are polynomials of one variable initialized via a list of coefficients. Instances are represented in the form (a(0))z^n + ... + (a(n-1))z + a(n), where [a(0),...,a(n)] is the initial list of coefficients and any a(i) may be equal to 0.0. 

This class includes several methods: 

-coeff(self, i) returns the coefficient corresponding to the variable raised to the ith power. For example, if the instance is 1.0z^2 + 0.0z + 2.0, coeff(0) will return 2.0, coeff(1) will return 0.0, and coeff(2) will return 1.0.

-add(self, other) will add the instance to the polynomial other and return the result. For example, if the instance is 1.0z^2 + 0.0z + 2.0 and other is 1.0z^3 + 0.0z^2 + 0.0z + 4.0, add(self, other) will return 1.0z^3 + 1.0z^2 + 0.0z + 6.0. This method can also be called via the addition symbol '+' between two instances. 

-mul(self, other) will multiply the polynomial with the polynomial other and return the result. For example, if the instance is 1.0z^2 + + 0.0z + 2.0 and other is 1.0z^3 + 0.0z^2 + 0.0z + 4.0, mul(self, other) will return 1.0z^5 + 0.0z^4 + 2.0z^3 + 4.0z^2 + 0.0z + 8.0. This method can also be called via the multiplication symbol '*'
