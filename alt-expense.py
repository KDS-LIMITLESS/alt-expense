# type: ignore
import datetime
from typing import  Dict, Union
  
class Expense:
  def __init__(self, expense_id: int, title: str, amount: int):
    self.expense_id = expense_id
    self.title = title
    self.amount = amount
    self.created_at = datetime.datetime.now()
    self.updated_at = datetime.datetime.now()

  def update(self, title: str, amount: int):
    self.title = title
    self.amount = amount
    self.updated_at = datetime.datetime.now()
    return self.to_dict()

  def to_dict(self) -> Dict[str, Union[int, str, datetime.datetime]]:
    return {
      "expense_id": self.expense_id,
      "title": self.title,
      "amount": self.amount,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }
  
  def __str__(self):
    return f"Expense ID: {self.expense_id}, Title: {self.title}, Amount: {self.amount}"
  




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








# Initialize expense_database
expense_db = ExpenseDatabase()

# Initialize expense items
expense_1 = Expense(1, "Testing Expense", 3000)
expense_2 = Expense(2, "Testing 2", 4000)

# Save expense data to database
expense_db.add_expense(expense_1)
expense_db.add_expense(expense_2)