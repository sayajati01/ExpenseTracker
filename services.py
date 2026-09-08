from utils import validate_id,validate_description,validate_category,validate_amount,validate_date
from models import Expense

def add_an_expense(expense_tracker):
    expense_id = validate_id()
    description = validate_description()
    category = validate_category()
    amount = validate_amount()
    date = validate_date()

    if expense_tracker.true_if_exists(expense_id):
        print("Expense is already in the database")
        input("Would you like to update instead? (y/n): ").lower().strip()
        if input in ['y','n']:
            if input == 'y':
                expense = expense_tracker.get_expense(expense_id)
                expense.update_expense(
                    description=description,
                    category=category, 
                    amount=amount, 
                    date=date
                    )
            print("Cancelling update, returning to menu\n")
            return
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

def find_expense(expense_tracker, action):
    expense_id = validate_id()
    if expense_tracker.true_if_exists(expense_id):
        expense = expense_tracker.get_expense(expense_id)
        expense.display_expense()
    print("Data Not Found.\n")

    if action=="Update" :
        update_expense(expense_tracker,expense)
    elif action=="Delete" :
        delete_expense(expense_tracker, expense)

def update_expense(expense_tracker, expense):
    return

def delete_expense(expense_tracker, expense):
    return

def view_all_expenses(expense_tracker):
    expense_tracker.display_expenses()

def view_statistics(expense_tracker):
    print(
        f"{'Total':<16} : {'Lorem Ipsum'}\n"
        f"{'Total':<16} : Rp {'Lorem Ipsum':,}\n"
        f"{'Total':<16} : Rp {'Lorem Ipsum':,}\n"
        f"{'Total':<16} : Rp {'Lorem Ipsum':,}\n"
        f"{'Total':<16} : Rp {'Lorem Ipsum':,}\n"
    )