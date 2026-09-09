import unittest
from models import ExpenseTrackerSystem,Expense
from datetime import datetime,timedelta
from services import delete_expense,add_an_expense,find_expense,update_expense,view_statistics,view_all_expenses
from unittest.mock import patch

class TestServices(unittest.TestCase):
    def setUp(self):
        self.expense_tracker = ExpenseTrackerSystem()
        self.date = datetime.now().replace(microsecond=0)
        self.expense = Expense("E122", "Lunch", "Food", 18000, self.date)
        self.expense_tracker.add_one_expense(self.expense)
    
    def test_delete_expense_after_adding(self):

        delete_expense(self.expense_tracker,self.expense)
        self.assertEqual(self.expense_tracker.expenses, {})

    def test_add_an_expense(self):
        expense_tracker = ExpenseTrackerSystem()

        with patch("builtins.input", side_effect=[
            "122",
            "Lunch",
            "Food",
            "18000"
        ]):
            add_an_expense(expense_tracker)

        expense = expense_tracker.get_expense("E122")

        self.assertEqual(expense.description, "Lunch")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.amount, 18000)

    def test_add_an_expense_with_duplicate_id(self):
        with patch("builtins.input", side_effect=[
            "122",
            "Dinner",
            "Pets",
            "9000",
            "n"
        ]):
            add_an_expense(self.expense_tracker)
            
            self.assertEqual(self.expense.description, "Lunch")
            self.assertEqual(self.expense.category, "Food")
            self.assertEqual(self.expense.amount, 18000)

        with patch("builtins.input", side_effect=[
            "122",
            "Dinner",
            "Pets",
            "9000",
            "y"
        ]):
            add_an_expense(self.expense_tracker)

        expense = self.expense_tracker.get_expense("E122")

        self.assertEqual(expense.description, "Dinner")
        self.assertEqual(expense.category, "Pets")
        self.assertEqual(expense.amount, 9000)

    def test_find_expense_with_action_None(self):

        with patch("builtins.input",return_value="122"):
            with patch("builtins.print") as mock_print:
                find_expense(self.expense_tracker)
                mock_print.assert_called()
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIn("E122", output)
                self.assertIn("Lunch", output)
                self.assertIn("Food", output)
                self.assertIn(str(18000), output)
                self.assertIn(str(self.date), output)

        with patch("builtins.input", return_value ="199"):
            with patch("builtins.print") as mock_print:
                find_expense(self.expense_tracker)
                mock_print.assert_called_once()
                output = mock_print.call_args[0][0]
                self.assertIn("Data Not Found.\n", output)

    def test_find_expense_with_action_update(self):

        with patch("builtins.input",side_effect=[
            "122",
            "Dinner",
            "Pets",
            9000
            ]):
            with patch("services.update_expense") as mock_update:
                find_expense(self.expense_tracker, "Update")
                mock_update.assert_called_once()

        with patch("builtins.input", side_effect=[
            "122",
            "Dinner",
            "Pets",
            9000
        ]):
            find_expense(self.expense_tracker, "Update")
            self.assertEqual(self.expense.description,"Dinner")
            self.assertEqual(self.expense.category,"Pets")
            self.assertEqual(self.expense.amount,9000)

    def test_find_expense_with_action_delete(self):

        with patch("builtins.input",return_value="122"):
            with patch("services.delete_expense") as mock_delete:
                find_expense(self.expense_tracker, "Delete")
                mock_delete.assert_called_once()

        with patch("builtins.input", return_value = "122"):
            find_expense(self.expense_tracker, action="Delete")
            self.assertEqual(self.expense_tracker.expenses, {})

    def test_view_all_expense(self):

        with patch.object(self.expense_tracker,"display_expenses") as mock_display:
            view_all_expenses(self.expense_tracker)
            mock_display.assert_called_once()

    def test_view_statistics(self):
        expense_2 = Expense(
            "E124",
            "Phone",
            "Electronics",
            3500000,
            self.date + timedelta(weeks=4)
        )
        self.expense_tracker.add_one_expense(expense_2)

        with patch("builtins.print") as mock_print:
            view_statistics (self.expense_tracker) 
            mock_print.assert_called_once()
            output = mock_print.call_args[0][0]
        print(output)

    def test_view_statistics_with_empty_expenses(self):
        self.expense_tracker.expenses = {}
        with patch("builtins.print") as mock_print:
            view_statistics (self.expense_tracker)
            mock_print.assert_called_once()
            output = mock_print.call_args[0][0]
            self.assertIn("No Data Found", output) 

                  

if __name__ == "__main__":
    unittest.main()