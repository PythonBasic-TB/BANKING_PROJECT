from decorators import print_f
from transfers import transfer_money
from view_acount import view_acc
from acount_creation import add_acount
from accaunt_data import database
from top_up_balance import top_up

#menu items # აქ შეგიძლიათ დაამატოთ პუნქტი, თავისი მნიშვნელობით, იგივე პუნქტს გამოვიყენებთ და განვსაზღვრავთ menu_actions-შიც
MENU_LIST = {
    "1": "Create new account",
    "2": "Top up balance",
    "3": "Transfer money",
    "4": "View account details",
    "5": "View account history",
    "6": "Calculate annual interest",
    "x": "Exit"
}
def menu_actions():
    print_f("Welcome to the Banking System!")
    menu_item =""
    while menu_item != "x":
        display_menu()    
        menu_item = input("Enter menu item: ")
        if menu_item == "1":
            add_acount(database)
            #add_acount (name, surname, balance, user_acount) 
            # ოთო აქ ოთხი პარამეტრი უნდა გააგზავნო, 
            #არ ჯობია უბრალოდ add_acount() და მერე შიგნით მოითხოვოს ინფორმაცია?
        elif menu_item == "2":
            top_up()
        elif menu_item == "3":
            transfer_money(database)
        elif menu_item == "4":
            view_acc(database)
        elif menu_item == "5":
            pass
        elif menu_item == "6":
            pass
        # აქ შეგვიძლია ვამატოთ სხვა ფუნქციების გამოძახება
        elif menu_item == "x":
            break
        else:
            print("Invalid menu item")
def display_menu():
    print("\n--- Menu List ---")
    for key,value in MENU_LIST.items():
        print(f"{key}. {value}")