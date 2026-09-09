from datetime import datetime, timedelta

class Expense:
    def __init__(self, expense_id :str, description:str, category:str, amount:int, date:datetime) -> None:
        self.expense_id = expense_id
        self.description = description
        self.category = category
        self.amount = amount
        self.date = date

    def update_expense(self, description:str=None, category:str=None, amount:int=None) -> None:
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if amount is not None:
            self.amount = amount
        print("Expense has been updated.\n")

    def display_expense(self) -> None:
        print(
            f"{'Expense ID':<18} : {self.expense_id}\n"
            f"{'Description':<18} : {self.description}\n"
            f"{'Category':<18} : {self.category}\n"
            f"{'Amount':<18} : {self.amount}\n"
            f"{'Date':<18} : {self.date}\n"
        )

class ExpenseTrackerSystem :
    def __init__(self) -> None:
        self.expenses = {}

    def add_one_expense(self, expense:Expense) -> None :
        self.expenses[expense.expense_id] = expense

    def display_expenses(self) -> None:
        if not self.expenses :
            print("No Data Found\n")
        for expense in self.expenses.values():
            print(
                f"{expense.expense_id:<7}|{expense.description:<20}|{expense.category:<15}|Rp {expense.amount:<8,}|{expense.date}|"
            )
        print()

    def true_if_exists(self, expense_id:str) -> bool:
        return expense_id in self.expenses

    def get_expense(self, expense_id:str) -> Expense:
        return self.expenses[expense_id]

    def del_expense(self, expense:Expense) -> None:
        print("Expense has been deleted\n")
        del self.expenses[expense.expense_id]