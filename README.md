# Polynomial-Class
Python class Polynomial for working with polynomials.

Instances of this class are polynomials of one variable initialized via a list of coefficients. Instances are represented in the form a(0)z\*\*n + ... + a(n-1)z + a(n), where [a(0),...,a(n)] is the initial list of coefficients and any a(i) may be equal to 0.0. Note that any integers in the initial list of coefficients will be converted into floating-point numbers. For example, Polynomial([1,0,2]) will create an instance represented as 1.0z\*\*2 + 0.0z + 2.0. 

This class includes five methods: 

1. coeff(self, i) returns the coefficient corresponding to the variable raised to the ith power. For example, if the instance is 1.0z\*\*2 + 0.0z + 2.0, coeff(self, 0) will return 2.0, coeff(self, 1) will return 0.0, and coeff(self, 2) will return 1.0.

2. add(self, other) will add the instance to the polynomial other and return the result. For example, if the instance is 1.0z\*\*2 + 0.0z + 2.0 and other is 1.0z\*\*3 + 0.0z\*\*2 + 0.0z + 4.0, add(self, other) will return a new instance 1.0z\*\*3 + 1.0z\*\*2 + 0.0z + 6.0. This method can also be called via the addition symbol '+' between two instances. 

3. mul(self, other) will multiply the instance with the polynomial other and return the result. For example, if the instance is 1.0z\*\*2 + + 0.0z + 2.0 and other is 1.0z\*\*3 + 0.0z\*\*2 + 0.0z + 4.0, mul(self, other) will return a new instance 1.0z\*\*5 + 0.0z\*\*4 + 2.0z\*\*3 + 4.0z\*\*2 + 0.0z + 8.0. This method can also be called via the multiplication symbol '\*' between two instances. 

4. val(self, v) will evaluate the instance with the variable set equal to v and return the result. For example, if the instance is 1.0z\*\*2 + 0.0z + 2.0, val(self, 3) will return 11.0 and val(self, 2.75) will return 9.5625. This method can also be called via function application: e.g. if poly is an instance, poly(3) will return the same result as poly.val(3). 

5. roots(self) will determine the roots of an instance of order 1 or 2, including complex roots, and return either the single root (if the instance has order 1) or a list containing two roots (if the instance has order 2). For example, if the instance is 1.0z\*\*2 + 4.0z + 4.0, roots(self) will return [-2.0, -2.0]. A polynomial of higher order will generate an error message, as will a polynomial of order 0 such as 0.0z + 3.0. Note that calling this method on instances of order 1 or 2 that were initialized with additional coefficients equal to 0.0 (e.g. Polynomial([0,0,1,4,4])) will modify those instances by removing the unnecessary terms and then evaluating them accordingly. For example, Polynomial([0,0,1,4,4]) will be converted by this method into an instance identical to Polynomial([1,4,4]) and then evaluated accordingly with result [-2.0, -2.0]. 
