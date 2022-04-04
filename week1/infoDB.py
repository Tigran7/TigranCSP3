InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "Name": "TigranArakelov",  
               "School": "Del Norte",  
               "City": "San Diego",  
               "Food": "Pizza",  
               "beverage": "Water",
               "sports":["Soccer","Basketball","Tennis","Hockey", "Track"]
              })

InfoDb.append({
    "Name": "Bob",
    "School": "Del Norte",
    "City": "San Diego",
    "Food": "Limes",
    "beverage": "Limeade",
    "sports":["Soccer", "Track"]
})

InfoDb.append({
    "Name": "Bill",
    "School": "Del Norte",
    "City": "San Diego",
    "Food": "Lemons",
    "beverage": "Lemon Juice",
    "sports":["","Lemon Squeezing"]
})

InfoDb.append({
    "Name": "Jeff",
    "School": "Del Norte",
    "City": "San Diego",
    "Food": "Rice",
    "beverage": "Rice Water",
    "sports":["Extreme Rice Washing"]
})

def print_data(n):
    print(InfoDb[n]["Name"], "lives in ", InfoDb[n]["City"])  # using comma puts space between values
    print("\t", "Food: ",(InfoDb[n]["Food"]))  # \t is a tab indent
    print("\t", "Beverage: ",(InfoDb[n]["beverage"]))
    print("\t", "Sports Played: ", end="")    #  end="" make sure no return occurs
    print(", ".join(InfoDb[n]["sports"]))  # join allows printing a string list with separator
    print()

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
      
def while_loop():
    n = 0
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
  
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def recur():
    recursive_loop(0)

def tester():
  print("forloop")
  for_loop()
  print("While loop")
  while_loop()
  print("Recursive loop")
  recursive_loop(0)

if __name__ == "__main__":
  tester()