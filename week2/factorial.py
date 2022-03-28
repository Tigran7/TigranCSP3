class Factorial:
    def __init__(self):
        self.factorialSeq = [1]
def __call__(self, n):
        if n < len(self.factorialSeq):
            return self.factorialSeq[n]
        else:
            # Compute the requested Fibonacci number
            fact_number = self(n - 1) + self(n - 2) # two recursive calls to self (__call__(self, n))
            self.factorialSeq.append(fact_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.factorialSeq[n]      

factorial_of = Factorial() # object instantiation and run __init__ method
print(factorial_of(5)) # object running __call__ method