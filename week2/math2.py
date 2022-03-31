def imp():
  a = int(input("First number in Arithmetic series: "))
  b = int(input("Amount of numbers in the series: "))
  c = int(input("Common difference between numbers in series: "))
  
  total = (b * (2 * a + (b - 1) * c)) / 2
  tn = a + (b - 1) * c
  
  print("The sum of the Arithmetic series = ", total)
  print("The n^th term in the series = ", tn)

class arith():
  def __init__(self):
    self.total = []
    self.tn = []
  def __call__(self, total, tn):
    a = int(input("First number in Arithmetic series: "))
    b = int(input("Second number in Arithmetic series: "))
    c = int(input("Common difference between numbers in series: "))
    
    self.total.append((b * (2 * a + (b - 1) * c)) / 2)
    return total
    self.tn.append(a + (b - 1) * c) 
    return tn
  