InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "Name": "TigranArakelov",  
               "School": "Del Norte",  
               "City": "San Diego",  
               "Food": "Pizza",  
               "beverage": "water",  
               "sports":["soccer","basketball","tennis","hockey", "Track"]  
              })

InfoDb.append({
    "Name": "Bob",
    "School": "Del Norte",
    "City": "San Diego",
    "Food": "Egg",
    "beverage": "water",
    "sports":["soccer", "Track"]
})

InfoDb.append({
    "Name": "Bill",
    "School": "Del Norte",
    "City": "San Diego",
    "Food": "Rice",
    "beverage": "Lemon",
    "sports":["basketball","tennis"]
})

InfoDb.append({
    "Name": "Jeff",
    "School": "Del Norte",
    "City": "San Diego",
    "Food": "Apple",
    "beverage": "Coke",
    "sports":["None"]
})

def print_data(n):
    print(InfoDb[n]["Name"], "lives in ", InfoDb[n]["City"])  # using comma puts space between values
    print("\t", "Food: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Food"]))  # join allows printing a string list with separator
    print("\t", "Beverage: ", end="")
    print(InfoDb[n].get("sports")[0])
    print()

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
      
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
  
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def tester():
  print("forloop")
  for_loop()
  print("While loop")
  while_loop(0)
  print("Recursive loop")
  recursive_loop(0)

if __name__ == "__main__":
  tester()