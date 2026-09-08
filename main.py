
from services import add_an_expense, find_expense, update_expense, delete_expense, view_all_expenses, view_statistics
from models import ExpenseTrackerSystem,Expense
from storage import save_data, load_data

def save_to_json(expense_tracker):
    return

def load_from_json():
    expense_tracker_raw = load_data()
    expense_tracker_system = ExpenseTrackerSystem()
    if not expense_tracker_raw:
        return expense_tracker_system

    for expense in expense_tracker_raw:
        expense_id = expense["Expense ID"]
        expense_description = expense["Description"]
        expense_category= expense["Category"]
        expense_amount = expense["Amount"]
        expense_date = expense["Date"]

        object_expense = Expense(
            expense_id,
            expense_description,
            expense_category,
            expense_amount,
            expense_date
            )

        expense_tracker_system.add_one_expense(object_expense)

    return expense_tracker_system

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
        "Statistics",
        "Exit"
    ]
    while running:

        print("============== Expense Tracker ==================")
        for index, menu in enumerate(menu_list, start=1):
            print(f"{index}. {menu}")
        choice = choose_menu(menu_list)
        if choice == 1:
            add_an_expense(expense_tracker)
        elif choice == 2:
            find_expense(expense_tracker)
        elif choice == 3 :
            update_expense(expense_tracker)
        elif choice == 4 :
            delete_expense(expense_tracker)
        elif choice == 5 :
            view_all_expenses(expense_tracker)
        elif choice == 6 :
            view_statistics(expense_tracker)
        elif choice == 7 :
            print("Good Bye!")
            break
main ()