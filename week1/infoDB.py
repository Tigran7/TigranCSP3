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

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({ 
               "Book_Title": "Outliers",  
               "Author": "Malcolm Gladwell",
               "Genre": "Nonfiction",
               "Published": "11/18/2008",  
               "Author_Books":["The Bomber Mafia", "What the Dog Saw", "Blink", "David and Goliath", "Talking to Strangers"]  
              })  
InfoDb.append({  
               "Book_Title": "Ready Player One",  
               "Author": "Ernest Cline",
               "Genre": "Science Fiction",
               "Published": "8/16/2011",  
               "Author_Books":["Ready Player Two", "Armada: A Novel", "The Importance of Being Ernest"]   
              })  
InfoDb.append({  
               "Book_Title": "Three Days of Happiness",  
               "Author": "Sugaru Miaki",
               "Genre": "Fiction",
               "Published": "12/25/2013",  
               "Author_Books":["Your Story", "The Place You Called From", "Parasite in Love", "Starting Over", "Pain, Pain, Go Away"]   
              })  
InfoDb.append({  
               "Book_Title": "No Longer Human",  
               "Author": "Osamu Dazai",
               "Genre": "Autobiographical Fiction",
               "Published": "1948 (No specific date)",  
               "Author_Books":["The Setting Sun", "Good Bye", "One Hundred Views of Mount Fuji", "The Late Years"]   
              })  


def print_data(n):
    print(InfoDb[n]["Name"], "lives in ", InfoDb[n]["city"])  # using comma puts space between values
    print("\t", "Food: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Food"]))  # join allows printing a string list with separator
    print("\t", "beverage: ", end="")
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