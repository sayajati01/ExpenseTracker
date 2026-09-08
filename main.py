
from services import add_an_expense, find_expense, update_expense, delete_expense, view_all_expenses
from models import ExpenseTrackerSystem

def choose_menu(menu_list):
    while True:
        try:
            choice = int(input(": "))
            if 0<choice<=len(menu_list):
                return choice
            print("INVALID MENU")
        except ValueError:
            print("INVALID MENU")

def main():
    expense_tracker = ExpenseTrackerSystem()
    running = True
    menu_list = [
        "Add an Expense",
        "Find Expense",
        "Update Expense",
        "Delete Expense",
        "View All Expenses",
        "Exit"
    ]
    while running:
        print("============== Expense Tracker ==================")
        for index, menu in enumerate(menu_list, start=1):
            print(f"{index}. {menu}")
        choice = choose_menu(menu_list)
        if choice == 1:
            add_an_expense()
        elif choice == 2:
            find_expense()
        elif choice == 3 :
            update_expense()
        elif choice == 4 :
            delete_expense()
        elif choice == 5 :
            view_all_expenses(expense_tracker)
        elif choice == 6 :
            print("Good Bye!")
            break
main ()