from w0 import swap
from w0 import matrix
from w0 import ship2
from w1 import database
from w1 import fibonacci
from w2 import factorial
from w2 import mathfunc

main_menu = [
    
]
#w 0 submenu
w0_list = [
    ["Swap", swap.age],
    ["Matrix", matrix.Matrix],
    ["Ironside Malphite", ship2.ship],
]
#w 1 submenu
w1_list = [
  ["Fibonacci", fibonacci.Fibonacci],
  ["Database", database.for_loop]
]

#w 2 submenu
w2_list = [
  ["Factorial", factorial.tstr],
  ["Arithmetic Sequence", mathfunc.imp],
]


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0",w0Menu])
    menu_list.append(["Week 1",w1Menu])
    menu_list.append(["Week 2",w2Menu])
    buildMenu(title, menu_list)
  

def w0Menu():
  title = "w 0 Menu" + banner
  buildMenu(title, w0_list)
  
def w1Menu():
  title = "w 1 Menu" + banner
  buildMenu(title, w1_list)

def w2Menu():
  title = "w 2 Menu" + banner
  buildMenu(title, w2_list)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])


    choice = input("Type your choice> ")


    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")

    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")


    buildMenu(banner, options) 


if __name__ == "__main__":
    menu()