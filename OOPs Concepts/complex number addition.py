class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __repr__(self):
        return f"ComplexNumber(real={self.real}, imag={self.imag})"
    
# Example usage
if __name__ == "__main__":
    c1 = ComplexNumber(2, 3)
    print(c1)  # Output: 2 + 3i
    
    c2 = ComplexNumber(4, 5)
    print(c2)  # Output: 4 + 5i
    
    print('-------')
    c3 = c1 + c2
    print(c3)  # Output: 6 + 8i
    print('-------')
    
    print(type(c3))  # Output: <class '__main__.ComplexNumber'>
    print(isinstance(c3, ComplexNumber))  # Output: True