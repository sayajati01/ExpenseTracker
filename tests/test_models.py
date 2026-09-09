import unittest
from models import Expense,ExpenseTrackerSystem
from datetime import datetime

class TestModels(unittest.TestCase):
    #=======================
    #
    #Test Cases for class Expense
    #
    #=======================
    def test_create_expense_no_false_input(self):
        date = datetime.now().replace(microsecond=0)
        expense = Expense("E122", "Lunch", "Food", 18000, date)
        expense_2 = Expense("E122", "Lunch", "Food", 18000, date)

        self.assertEqual(expense.expense_id, "E122")
        self.assertEqual(expense.description, "Lunch")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.amount, 18000)
        self.assertEqual(expense.date, date)
        self.assertEqual(expense, expense_2)

    def test_update_one_expense_no_false_input(self):
        date = datetime.now().replace(microsecond=0)
        expense = Expense("E122", "Lunch", "Food", 18000, date)

        expense.update_expense(
            description = "Dinner",
            category = "Family",
            amount = 1000000
        )

        self.assertEqual(expense.description, "Dinner")
        self.assertEqual(expense.category, "Family")
        self.assertEqual(expense.amount, 1000000)
        self.assertEqual(expense.date, date)

    def test_update_only_description_no_false_input(self):
        date = datetime.now().replace(microsecond=0)
        expense = Expense("E122", "Lunch", "Food", 18000, date)

        expense.update_expense(
            description="Breakfast"
        )
        self.assertEqual(expense.description, "Breakfast")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.amount, 18000)
        self.assertEqual(expense.date, date)

    def test_update_only_category_no_false_input(self):
        date = datetime.now().replace(microsecond=0)
        expense = Expense("E122", "Lunch", "Food", 18000, date)
        expense.update_expense(
            category="Drink"
        )
        self.assertEqual(expense.description, "Lunch")
        self.assertEqual(expense.category, "Drink")
        self.assertEqual(expense.amount, 18000)
        self.assertEqual(expense.date, date)

    def test_update_only_amount_no_false_input(self):
        date = datetime.now().replace(microsecond=0)
        expense = Expense("E122", "Lunch", "Food", 18000, date)
        expense.update_expense(
            amount=20000
        )
        self.assertEqual(expense.description, "Lunch")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.amount, 20000)
        self.assertEqual(expense.date, date)

    #=========================
    #
    #TestCases for class ExpenseTrackerSystem
    #
    #=========================
    def test_add_one_expense_no_false_input(self):
        expense_system = ExpenseTrackerSystem()
        date = datetime.now().replace(microsecond=0)
        expense = Expense("E122", "Lunch", "Food", 18000, date)

        expense_system.add_one_expense(expense)
        is_exists = expense_system.true_if_exists(expense.expense_id)

        self.assertEqual(expense_system.expenses[expense.expense_id], expense)
        self.assertEqual(expense_system.get_expense(expense.expense_id), expense)
        self.assertEqual(is_exists, True)

    def test_delete_expense_no_false_inpnut(self):
        expense_system = ExpenseTrackerSystem()
        date = datetime.now().replace(microsecond=0)
        expense = Expense("E122", "Lunch", "Food", 18000, date)
        expense_system.add_one_expense(expense)
        expense_system.del_expense(expense)

        self.assertEqual(expense_system.expenses, {})



if __name__ == "__main__" :
    unittest.main()
