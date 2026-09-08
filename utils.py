from datetime import datetime

def validate_id():
    while True:
        id_digit = input("ID (3 digit):").lower().strip()
        if id_digit.isdigit() and len(id_digit)==3:
            expense_id = "E"+id_digit
            return expense_id
        print("INVALID ID)")

def validate_description():
    while True:
        description = input("Desc : ").strip()
        if description != "" and len(description)<=20 and not description.isdigit():
            return description
        print("INVALID CATEGORY")

def validate_category():
    categories = [
            "Food",
            "Drink",
            "Other"
            ]

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        category = input("Choose category (or type a new one) : ").title().strip()
        if category in categories :
            return category
        elif len(category)<=15 and category != "" :
            return category
        print("INVALID CATEGORY")

def validate_amount():
    while True :
        try:
            amount = int(input("Amount : "))
            if 500<=amount:
                return amount
            print("INVALID AMOUNT")
        except ValueError:
            print("INVALID AMOUNT")

def validate_date():
    return datetime.now().replace(microsecond=0)