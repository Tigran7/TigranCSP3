from simple_term_menu import TerminalMenu

options = ["[a] optionOne", "[b] OptionThree", "[c] OptionFour", "[q] Quit"]

mainMenu = TerminalMenu(options, title = "main menu")
subMenu = TerminalMenu(["[d] first", "[e] second"], title = "sub-menu")

quitting = False

while quitting == False:
  optionsIndex = mainMenu.show()
  optionsChoice = options[optionsIndex]

  if(optionsChoice == "[q] Quit"):
    quitting = True
  if(optionsChoice == "[c] OptionFour"):
    subMenu.show()
  else:
    print(optionsChoice)