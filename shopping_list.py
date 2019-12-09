def mainScreen():
    os.system('cls')
    print("######################")
    print("     SHOPPING LIST     ")
    print("#######################")
    print("Your list contains",len(shop),"items.")
    print("Please choose from the following options:")
    print("(a)dd to the list")
    print("(d)elete from the list")
    print("(v)iew from the list")
    print("(q)uit the program")
    choice = input("choice: ")
    if len(choice) > 0:
        if choice.lower().startswith("a"):
            addScreen()
        elif choice.lower().startswith("d"):
            deleteScreen()
        elif choice.lower().startswith("v"):
            viewScreen()
        elif choice.lower().startswith("q"):
            sys.exit()
        else:
            mainScreen()
    else:
        mainScreen()

def addScreen():
    os.system('cls')
    print("######################")
    print("    ADDING LIST SCREEN  ")
    print("#######################")
    print("\n\n")
    print("Please enter the name of the item you wnat to add.")
    print( "Press ENTER to return to the main menu.\n")
    item = input("\nItem: ")
    if len(item) > 0:
        shop.append(item)
        print("item has been locked in GLEE :)")
        time.sleep(1)
        addScreen()
    else:
        mainScreen()

    

def viewScreen():
    os.system('cls')
    print("######################")
    print("     VIEW LIST SCREEN    ")
    print("#######################")
    print("\n\n")
    for item in shop:
        print(item)
    
    print("\n\n")
    print(" press ENTER to return to main menu.\n")
    input()
    mainScreen()

def deleteScreen():
    os.system('cls')
    print("######################")
    print("     DELETE SCREEN LIST  ")
    global shop
    os.system('cls')
    print("######################")
    print("     DELETE SCREEN LIST  ")
    print("#######################")
    count = 0
    for item in shop:
        print(count, "-", item)
        count = count + 1
    print("What number do you want to delete?")
    choice = input("number:  ")
    if len(choice) > 0:
        try:
            del shop[int(choice)]
            print("item deleted... sad to see it go so soon.")
            time.sleep(1)
        except:
            print("invalid option for deletion.")
            time.sleep(1)
        deleteScreen()
    else:
        mainScreen()
print("Welcome to CameronShoppinglist.py")
shopping_list = []
add= input("Want to add something to your shopping list? Y or N")

while add.lower() == lower "sure":
    item = input("enter your new item to the list:")
    shopping_list.append(item)
    add = input("Want to add to your shopping list? Y or N")
print()
print("Here is your shopping list in aplphabetical order")
shopping_list.sort()
for listitem in shopping_list:
    print(listitem)
    
    
def remove_item(idx):
    index = idx -1
    item = shopping_list.pop(index)
    print("Remove {}.".format(item))

def show_help():
    print("\nSeparate each item with a comma.")
    print("Type DONE to quit, SHOW to see the current list, REMOVE to delete an d item and HELP to get this message")


def show_list():
    count = 1
    for item in shopping_list:
        print ("{}: {}".format(count, item))
        count += 1

print("Give me a list of things you want to shop for.")
show_help()

while True:
    new_stuff = input("> ")

    if new_stuff == "DONE":
        print("\nHere's your list:")
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    elif new_stuff == "REMOVE":
        show_list()
        idx = input("Which item? Tell me the number.")
        remove_item(int(idx))
        continue
    else:
        new_list = new_stuff.split(",")
        index = input("Add this at a certain spot? Press enter for the end of the list, "
                                    "or give me a number. Currently {} item in the list.".format(
                       len(shopping_list)))
        if index:
            spot = int(index) -1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())


