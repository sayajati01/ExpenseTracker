from datetime import datetime, timedelta

class Expense:
    def __init__(self, expense_id, description, category, amount, date):
        self.expense_id = expense_id
        self.description = description
        self.category = category
        self.amount = amount
        self.date = date

    def update_expense(self, description="", category="Other", amount=0, date=datetime.now()):
        self.description = description
        self.category = category
        self.amount = amount
        self.date = date

    def display_expense(self):
        print(
            f"{'Expense ID':<18} : {self.expense_id}\n"
            f"{'Description':<18} : {self.description}\n"
            f"{'Category':<18} : {self.category}\n"
            f"{'Amount':<18} : {self.amount}\n"
            f"{'Date':<18} : {self.date}\n"
        )

class ExpenseTrackerSystem :
    def __init__(self):
        self.expenses = {}

    def add_one_expense(self, expense):
        self.expenses[expense.expense_id] = expense

    def display_expenses(self):
        if not self.expenses :
            print("No Data Found\n")
        for expense in self.expenses.values():
            print(
                f"{self.expense.expense_id:<7}{expense.description:<20}{expense.category:<15}{expense.amount:,<8}{expense.date:<10}"
            )
        