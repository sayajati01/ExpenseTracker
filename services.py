from utils import validate_id,validate_description,validate_category,validate_amount,validate_date
from models import Expense,ExpenseTrackerSystem

def add_an_expense(expense_tracker:ExpenseTrackerSystem) -> None:
    expense_id = validate_id()
    description = validate_description()
    category = validate_category()
    amount = validate_amount()
    date = validate_date()

    if expense_tracker.true_if_exists(expense_id):
        print("Expense is already in the database")
        want_update = input("Would you like to update instead? (y/n): ").lower().strip()
        if want_update in ['y','n']:
            if want_update == 'y':
                expense = expense_tracker.get_expense(expense_id)
                expense.update_expense(
                    description=description,
                    category=category, 
                    amount=amount,
                    )
                expense.display_expense()
            else :
                print("Cancelling update, returning to menu\n")
            return
        else:
            print("Invalid Menu, returning to menu\n")
        return

    expense = Expense(
        expense_id,
        description,
        category,
        amount,
        date
    )
    print("New Expense Created")
    expense.display_expense()
    expense_tracker.add_one_expense(expense)

def find_expense(expense_tracker:ExpenseTrackerSystem, action:str=None) -> None:
    expense_id = validate_id()
    expense = None
    if expense_tracker.true_if_exists(expense_id):
        expense = expense_tracker.get_expense(expense_id)
        expense.display_expense()
    else :
        print("Data Not Found.\n")

    if action is not None:
        if action=="Update" and expense is not None:
            update_expense(expense)
            expense.display_expense()
        elif action=="Delete" and expense is not None:
            delete_expense(expense_tracker, expense)
        else :
            print(f"{action} Cancelled.")

def update_expense(expense:Expense) -> None:
    description = validate_description()
    category = validate_category()
    amount = validate_amount()

    expense.update_expense(
        description=description,
        category=category, 
        amount=amount,
        )
    
def delete_expense(expense_tracker:ExpenseTrackerSystem, expense:Expense) -> None:
    expense_tracker.del_expense(expense)

def view_all_expenses(expense_tracker:ExpenseTrackerSystem) -> None:
    expense_tracker.display_expenses()

def view_statistics(expense_tracker:ExpenseTrackerSystem) -> None:
    if not expense_tracker.expenses:
        print("No Data Found\n")
        return

    highest = max(
        expense_tracker.expenses.values(),
        key=lambda expense: expense.amount
    )
    lowest = min(
        expense_tracker.expenses.values(),
        key=lambda expense: expense.amount
    )
    print(
        f"{'Total Expenses':<16} : {len(expense_tracker.expenses)}\n"
        f"{'Total Spending':<16} : Rp {sum(expense.amount for expense in expense_tracker.expenses.values()):,}\n"
        f"{'Average Expense':<16} : Rp {int(sum(expense.amount for expense in expense_tracker.expenses.values())/len(expense_tracker.expenses)):,}\n"
        f"{'Highest Expense':<16} : Rp {highest.amount:,}\n"
        f"{'Lowest Expense':<16} : Rp {lowest.amount:,}\n"
    )