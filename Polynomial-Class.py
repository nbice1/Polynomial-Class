class Polynomial:
    def __init__(self, coefficients):
        coeffs = []
        for r in coefficients:
            coeffs.append(float(r))
        self.coeffs = coeffs
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
    def coeff(self, i):
        if 0 <= i < len(self.coeffs):
            return self.coeffs[-1 - i]
        else:
            return 0.0
    def add(self, other):
        rev_poly = []
        rev_self_coeffs = self.coeffs[::-1]
        rev_other_coeffs = other.coeffs[::-1]
        for n in range(len(rev_self_coeffs)):
            if n <= len(rev_other_coeffs) - 1:
                rev_poly.append(rev_self_coeffs[n] + rev_other_coeffs[n])
            else:
                rev_poly.append(rev_self_coeffs[n])
        if len(rev_other_coeffs) > len(rev_self_coeffs):
            for n in range(len(rev_self_coeffs), len(rev_other_coeffs)):
                rev_poly.append(rev_other_coeffs[n])
        new_poly = rev_poly[::-1]
        return Polynomial(new_poly)
    def __add__(self, other):
        return self.add(other)
    def mul(self, other):
        new_poly = Polynomial([0])
        rev_self_coeffs = self.coeffs[::-1]
        rev_other_coeffs = other.coeffs[::-1]
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
    def val(self, v):
        rev_self_coeffs = self.coeffs[::-1]
        value = 0
        for n in range(len(rev_self_coeffs)):
            value = value + rev_self_coeffs[n]*(v**(n))
        return value
    def __call__(self, v):
        return self.val(v)
    def roots(self):
        if len(self.coeffs) == 1:
            print ("Root does not exist.")
        elif len(self.coeffs) > 3:
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
            if self.coeffs[0] == 0:
                print ("Root does not exist.")
            else: 
                root = (0 - self.coeffs[1]) / self.coeffs[0]
                return root
        else:
            a = self.coeffs[0]
            b = self.coeffs[1]
            c = self.coeffs[2]
            if a == 0:
                if b == 0:
                    print ("Root does not exist.")
                    return None
                else:
                    return -c / b
            elif b**2 < 4*a*c:
                root1 = (-b + complex((b**2 - 4*a*c),0)**0.5) / (2*a)
                root2 = (-b - complex((b**2 - 4*a*c),0)**0.5) / (2*a)
            else:
                root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
                root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
            result = [root1, root2]
            return result
