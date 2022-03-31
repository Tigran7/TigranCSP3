#no longer used until you fix maybe? C:
class Math:
    def __init__(self):
        self.mSeq = [1]
def __call__(self):
        if self < len(self.mSeq):
            return self.mSeq[self]
        else:
            # Compute the requested Fibonacci number
            ma_number = self * 2 +1
            self.mSeq.append(ma_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.mSeq[self]      

m_of = Math() # object instantiation and run __init__ method
print(m_of(5)) # object running __call__ method