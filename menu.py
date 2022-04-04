from week0 import swap
from week0 import numpad
from week1 import infoDB
from week1 import fibonacci
from week2 import factorial
from week2 import math2
from my_projects import physics

main_menu = [
    
]
#w 0 submenu
w0_list = [
    ["Swap", swap.age],
    ["Numpad", numpad.Matrix],
# When you make a new thing? you can use this  list format format C:
]
#w 1 submenu
w1_list = [
  ["Fibonacci", fibonacci.fibo],
  ["Database (This will print using all three methods)", infoDB.tester]
]
alt_list = [
    ["Database For Loop", infoDB.for_loop],
    ["Database While Loop", infoDB.while_loop],
    ["Database Recursive Loop", infoDB.recur],
]

#w 2 submenu
w2_list = [
  ["Factorial", factorial.tstr],
  ["Arithmetic Sequence", math2.imp],
]

w3_list = [
  ["Physics", physics.go],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0",w0Menu])
    menu_list.append(["Week 1",w1Menu])
    menu_list.append(["Week 2",w2Menu])
    menu_list.append(["My Projects",w3Menu])
    buildMenu(title, menu_list)
  

def w0Menu():
  title = "week 0 Menu" + banner
  buildMenu(title, w0_list)
  
def w1Menu():
  title = "week 1 Menu" + banner
  w1_list.append(["Database alternate printing options", altMenu],)
  buildMenu(title, w1_list)

def altMenu():
  title = "Alternate Printing Options" + banner
  buildMenu(title, alt_list)

def w2Menu():
  title = "week 2 Menu" + banner
  buildMenu(title, w2_list)

def w3Menu():
  title = "My Projects" + banner
  buildMenu(title, w3_list)


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