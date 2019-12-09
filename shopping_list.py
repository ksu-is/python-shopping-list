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
mainScreen()
time.sleep(1)
addScreen()
time.sleep(1)
viewScreen()
time.sleep(1)


print("Here is your shopping list in aplphabetical order")
shopping_list.sort()
for listitem in shopping_list:
    print(listitem)


