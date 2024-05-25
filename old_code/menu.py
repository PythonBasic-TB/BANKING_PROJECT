from decorators import print_f
from top_up_balance import top_up
from transfers import transfer_money
from view_acount import view_acc
from acount_creation import add_acount
from accaunt_data import account_database as database, t_h
from calculate_anual_interest import cal_anual_int
from transaction_history import view_history
from view_file import view_file
from full_hist import hist


#menu items # აქ შეგიძლიათ დაამატოთ პუნქტი, თავისი მნიშვნელობით, იგივე პუნქტს გამოვიყენებთ და განვსაზღვრავთ menu_actions-შიც
MENU_LIST = {
    "1": "Create new account",
    "2": "Top up balance",
    "3": "Transfer money",
    "4": "View account details",
    "5": "View account history",
    "6": "view file",
    "7": "Calculate annual interest",
    "8": "view full history",
    "x": "Exit"
}
def menu_actions():
    print_f("Welcome to the Banking System!")
    menu_item =""
    f ='transactions.txt'
    while menu_item != "x":
        display_menu()    
        menu_item = input("Enter menu item: ")
        if menu_item == "1":
            add_acount(database)
            #add_acount (name, surname, balance, user_acount) 
            # ოთო აქ ოთხი პარამეტრი უნდა გააგზავნო, 
            #არ ჯობია უბრალოდ add_acount() და მერე შიგნით მოითხოვოს ინფორმაცია?
        elif menu_item == "2":
            top_up(database, t_h)
        elif menu_item == "3":
            transfer_money(database)
        elif menu_item == "4":
            view_acc(database)
        elif menu_item == "5":
            view_history (t_h) 
        elif menu_item == "6":
            view_file (f)
        elif menu_item == "7":
            cal_anual_int(database, t_h)
        elif menu_item == "8":
            hist(t_h)
        # აქ შეგვიძლია ვამატოთ სხვა ფუნქციების გამოძახება
        elif menu_item == "x":
            break
        else:
            print("Invalid menu item")
def display_menu():
    print("\n--- Menu List ---")
    for key,value in MENU_LIST.items():
        print(f"{key}. {value}")