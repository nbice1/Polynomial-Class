#class for working with polynomials, initialized with a list of coefficients (integers are converted to floats)
class Polynomial:
    def __init__(self, coefficients):
        coeffs = []
        for r in coefficients:
            coeffs.append(float(r))
        self.coeffs = coeffs
        
    #string representation of polynomials of the form 'a(0)z**n +...+ a(n-1)z + a(n)', where a(i) are the coeffs
    def __str__(self):
        string = ""
        add_str = " + "
        for n in range(len(self.coeffs)):
            n_coeff = str(self.coeffs[n])
            if n < len(self.coeffs) - 2:
                string = string + n_coeff + "z**"+ \
                str(len(self.coeffs) - n - 1) + add_str
            elif n < len(self.coeffs) - 1:
                string = string + n_coeff + "z" + add_str
            else:
                string = string + n_coeff
        return string
    def __repr__(self):
        return str(self)
    
    #method returns the coefficient attached to the variable raised to the ith power
    def coeff(self, i):
        if 0 <= i < len(self.coeffs):
            return self.coeffs[-1 - i]
        else:
            return 0.0

    #method for adding two polynomials and returning their sum
    def add(self, other):
        rev_poly = []
        rev_self_coeffs = self.coeffs[::-1]
        rev_other_coeffs = other.coeffs[::-1]
        
        #loops over reversed lists of coeffs, adding together coeffs at the same position in the list (corresponding to the 
        #variable raised to the same power), followed by adding extra terms in case the initial polynomial has higher degree
        for n in range(len(rev_self_coeffs)):
            if n <= len(rev_other_coeffs) - 1:
                rev_poly.append(rev_self_coeffs[n] + rev_other_coeffs[n])
            else:
                rev_poly.append(rev_self_coeffs[n])
                
        #if condition catches extra terms in case the second polynomial has higher degree
        if len(rev_other_coeffs) > len(rev_self_coeffs):
            for n in range(len(rev_self_coeffs), len(rev_other_coeffs)):
                rev_poly.append(rev_other_coeffs[n])
                
        #the new list of coeffs is created by reversing the constructed list rev_poly, followed by returning the new 
        #initialized polynomial
        new_poly = rev_poly[::-1]
        return Polynomial(new_poly)
    def __add__(self, other):
        return self.add(other)
    
    #method for multiplying two polynomials and returning the resulting polynomial
    def mul(self, other):
        #begins by constructing a new polynomial new_poly (corresponding to '0.0') that will be added to 
        #and reversing both lists of coeffs
        new_poly = Polynomial([0])
        rev_self_coeffs = self.coeffs[::-1]
        rev_other_coeffs = other.coeffs[::-1]
        
        #loops over reversed list of coeffs, constructing the new polynomial term by term, first multiplying the z**0-term 
        #by each term of the second polynomial and then adding the resulting polynomial to new_poly, 
        #then multiplying the z**1-term by each term of the second polynomial and then adding the result to new_poly, etc. 
        #This is done via list comprehensions, noting that e.g. the polynomial resulting from multiplying the z**2-term by 
        #each term of the second polynomial can be initialized by multiplying each coefficient of the second polynomial by 
        #z**2's coefficient followed by adding two 0's to the end of the new list of coeffs. 
        for n in range(len(rev_self_coeffs)):
            if n == 0:
                rev_poly_term = [r * rev_self_coeffs[n] for \
                r in rev_other_coeffs]
            else:
                rev_poly_term = [0 for m in range(n)] + \
                [r * rev_self_coeffs[n] for r in rev_other_coeffs]
            poly_term = rev_poly_term[::-1]
            new_poly = new_poly + Polynomial(poly_term)
        return new_poly
    def __mul__(self, other):
        return self.mul(other)
    
    #method for evaluating a polynomial by setting the variable z equal to the input value v
    def val(self, v):
        rev_self_coeffs = self.coeffs[::-1]
        value = 0
        
        #loops over reversed list of coeffs, adding the corresponding term with z = v to the variable 'value', which is 
        #then returned
        for n in range(len(rev_self_coeffs)):
            value = value + rev_self_coeffs[n]*(v**(n))
        return value
    def __call__(self, v):
        return self.val(v)
    
    #finds the roots of a polynomial of order 2 or less
    def roots(self):
        if len(self.coeffs) == 1:
            print ("Root does not exist.")
        elif len(self.coeffs) > 3:
            #checks a polynomial of more than 3 terms to see if the additional terms are equal to 0, at which point the 
            #additional terms are deleted from the instance and the method is called again; otherwise prints an error message
            rev_self_coeffs = self.coeffs[::-1]
            result = True
            for n in range(3,len(rev_self_coeffs)):
                result = result and rev_self_coeffs[n] == 0
            if result:
                rev_self_coeffs = rev_self_coeffs[:3]
                self.coeffs = rev_self_coeffs[::-1]
                return self.roots()
            else:
               print ("Order too high to solve for roots.")
        elif len(self.coeffs) == 2:
            #checks a polynomial of two terms to see if the z-term is equal to 0, at which point it prints an error message;
            #otherwise computes the root and returns it
            if self.coeffs[0] == 0:
                print ("Root does not exist.")
            else: 
                root = (0 - self.coeffs[1]) / self.coeffs[0]
                return root
        else:
            a = self.coeffs[0]
            b = self.coeffs[1]
            c = self.coeffs[2]
            
            #checks a polynomial of three terms to see if the z**2-term is equal to zero, at which point it prints an error 
            #message if the z-term is equal to 0 as well and otherwise computes the result and returns it
            if a == 0:
                if b == 0:
                    print ("Root does not exist.")
                    return None
                else:
                    return -c / b
                
            #if the polynomial has order two, uses the quadratic formula to find its pair of roots (possibly the same), which
            #may be complex numbers; returns a list containing the roots
            elif b**2 < 4*a*c:
                root1 = (-b + complex((b**2 - 4*a*c),0)**0.5) / (2*a)
                root2 = (-b - complex((b**2 - 4*a*c),0)**0.5) / (2*a)
            else:
                root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
                root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
            result = [root1, root2]
            return result
