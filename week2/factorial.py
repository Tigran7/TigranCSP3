class Factorial:
  def __init__(self):
    self.factorial = [1,1]
    
  def __call__ (self,num):
    if num <= 1:
      pass #goes to the end return statement
    else:
      self.factorial.append(num * self(num-1)) 
    return self.factorial[num]


#Output function
def tstr():
  #Num set here instead of user input, can change
  num = 5
  g = Factorial()
  print("The factorial of",num, "is", g(num))
