# type: ignore
from datetime import datetime, timezone
import uuid
import pytz
from typing import  Dict, Union

dt = datetime.now(timezone.utc) 
  
utc_time = dt.replace(tzinfo=timezone.utc) 
utc_timestamp = utc_time.timestamp() 
  
class Expense:
  def __init__(self, title: str, amount: float):
    self.expense_id = uuid.uuid4().int
    self.title = title
    self.amount = amount
    self.created_at = utc_timestamp
    self.updated_at = utc_timestamp

  def update(self, title: str, amount: float):
    self.title = title
    self.amount = amount
    self.updated_at = utc_timestamp
    return self

  def to_dict(self) -> Dict[str, Union[int, str, datetime]]:
    return {
      "expense_id": self.expense_id,
      "title": self.title,
      "amount": self.amount,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }
  
  def __str__(self):
    return f"Expense ID: {self.expense_id}, Title: {self.title}, Amount: {self.amount}, Updated_At: {self.updated_at}"
  


# Expense Database

class ExpenseDatabase:
  def __init__(self) -> None:
    self.expenses = {}

  def add_expense(self, expense: Expense):
    self.expenses[expense.expense_id] = expense
    return expense.to_dict()

  def remove_expense(self, expense_id: int):
    expense: Expense
    for expense in self.expenses.values():
      if expense.expense_id == expense_id:
        return self.expenses.pop(expense.expense_id)
    return 'Expense not found'
  
  def get_expense(self, expense_id: int) -> Union[Expense, None]:
    return self.expenses.get(expense_id)
  
  def get_expense_by_title(self, expense_title: str):
    expense: Expense
    expense_list = []
    for expense in self.expenses.values():
      if expense.title == expense_title:
        expense_list.append(expense.to_dict())
    return expense_list 

  def to_dict(self):
    expense_list: list[Expense] = []
    for expense in self.expenses.values():
      expense_list.append(expense.to_dict()) 
    return expense_list



# ************Initialize Project ***********

# Initialize expense_database
expense_db = ExpenseDatabase()

# Initialize expense items
expense_1 = Expense("Testing Expense", 3000.0)
expense_2 = Expense("Testing 2", 4000.0)

# Save expense data to database
expense_db.add_expense(expense_1)
expense_db.add_expense(expense_2) 

# Expense class methods

print(expense_1.update("Updating expense 1", 3000.0))
print(expense_2.to_dict())


# Expense database methods 

print(expense_db.remove_expense(1))
print(expense_db.get_expense(317207130060184451509440739815726307525))
print(expense_db.get_expense_by_title("Testing Expense"))
print(expense_db.to_dict())