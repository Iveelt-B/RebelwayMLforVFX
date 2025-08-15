from dataclasses import dataclass, field
from datetime import date, timedelta
from library_cart.random_number_utils import RandomUtils

@dataclass
class Book:
	title: str
	author: str
	due_days: int
	borrow_date: date = None

	def borrow(self):
		self.borrow_date = date.today()

	def due_date(self):
		if not self.borrow_date:
			return None
		return self.borrow_date + timedelta(days=self.due_days)

	def is_overdue(self):
		if not self.borrow_date:
			return False
		return data.today() > self.due_date()

