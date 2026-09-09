from datetime import datetime
from models import Categories

def validate_id() -> str:
    while True:
        id_digit = input("ID (3 digit):").lower().strip()
        if id_digit.isdigit() and len(id_digit)==3:
            expense_id = "E"+id_digit
            return expense_id
        print("INVALID ID)")

def validate_description() -> str:
    while True:
        description = input("Desc : ").strip()
        if description != "" and len(description)<=20 and not description.isdigit():
            return description
        print("INVALID CATEGORY")

def validate_category() -> str:
    Categories.display_categories()
    
    while True:
        category = input("Type one of above category (or type a new one) : ").title().strip()
        if category in Categories :
            return category
        print("INVALID CATEGORY")

def validate_amount() -> int:
    while True :
        try:
            amount = int(input("Amount : "))
            if 500<=amount:
                return amount
            print("INVALID AMOUNT")
        except ValueError:
            print("INVALID AMOUNT")

def validate_date() -> datetime:
    return datetime.now().replace(microsecond=0)