def fibo():
#Python program to generate Fibonacci series until 'n' value
  n = int(input("Enter the value of 'n': "))
  a = 0
  b = 1
  sum = 0
  count = 1
  print("Fibonacci Series: ", end = " ")
  while(count <= n):
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b
  # Program to display the Fibonacci sequence up to n-th term
  
  nterms = int(input("How many terms? "))
  
  # first two terms
  n1, n2 = 0, 1
  count = 0
  
  # check if the number of terms is valid
  if nterms <= 0:
     print("Please enter a positive integer")
  elif nterms == 1:
     print("Fibonacci sequence upto",nterms,":")
     print(n1)
  else:
     print("Fibonacci sequence:")
     while count < nterms:
         print(n1)
         nth = n1 + n2
         # update values
         n1 = n2
         n2 = nth
         count += 1
