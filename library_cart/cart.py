import json
from dataclasses import dataclass, field
from library_cart.book import Book
from library_cart.random_number_utils import RandomUtils
from library_cart.file_io import Fstream
from datetime import datetime, timedelta

@dataclass
class LibraryCart:
	database_path: str
	isEmpty: bool = True
	isActive: bool = False
	id: str = field(init=False, default_factory=RandomUtils.generate_random_id)

	def get_all_books(self, verbose=0) -> dict:
	"""
	Reads and returns a hash map with all the available borrowed books.
        If verbose is set to 1, it will print all the books.
	"""
	data_file = Fstream.load_json_files(self.database_path)

	if len(data_file["Books"].items()) > 0:
            	self.isEmpty = False
            	self.isActive = True

	try: 
		verbose == 1:
		Fstream.print_json_structure(data_file)
		return data_file
	else:
		return data_file
	except:
		raise ValueError(The value for verbose must be 0 or 1)
def search_books(self, query: str) -> list[Book]
	"""
	Search borrowed books by title or author.
	"""
	data = Fstream.load_json_files(self.database_path)
        matching_books = []

	for book_id, book_data in data["Books"].items():
            	book = Book(title=book_data["title"], author=book_data["author"], 
                	borrow_date=book_data["borrow_date"], 
                        return_date=book_data["return_date"], id=book_id)
            	if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                	matching_books.append(book)	
	if not matching_books:
            	print("No books found")
        else:
            	for book in matching_books:			
			print(f"Found: {book.title} by {book.author} (Due: {book.return_date})")
	return matching_books

def get_total_book_count(self) -> int:
	"""
	Returns the total number of borrowed books.
	"""
	data = self.get_all_books()
	return len(data["Books"].items())
	
def borrow_book(self, book: Book, days_to_return=14):
        """
        Borrow a book and update the database.json file.
        """
        data = self.get_all_books()
        return_date = (datetime.now() + timedelta(days=days_to_return)).strftime("%Y-%m-%d")

        new_book = {
        	"title": book.title,
		"author": book.author,
		"borrow_date": datetime.now().strftime("%Y-%m-%d"),
            	"return_date": return_date
        }

	data["Books"][book.id] = new_book

        with open(self.database_path, 'w') as file:
            	json.dump(data, file, indent=4)

        self.isEmpty = False
        self.isActive = True

	print(f"Borrowed '{book.title}' by {book.author}. Return by {return_date}.")

def return_book_by_query(self, query: str):
        """
        Return a borrowed book based on a title or author search.
        """
        data = self.get_all_books()
        items_to_remove = []

        for book_id, book_data in data["Books"].items():
            if query.lower() in book_data["title"].lower() or query.lower() in book_data["author"].lower():
                items_to_remove.append(book_id)

        if not items_to_remove:
            print(f"No borrowed book found matching '{query}'")
            return

        for book_id in items_to_remove:
            book_title = data["Books"][book_id]["title"]
            del data["Books"][book_id]
            print(f"Returned '{book_title}'.")

	with open(self.database_path, 'w') as file:
            json.dump(data, file, indent=4)

        if not data["Books"]:
            self.isEmpty = True
            self.isActive = False

def check_due_dates(self):
        """
        Check if any borrowed books are overdue.
        """
        data = self.get_all_books()
        today = datetime.now()

        for book_id, book_data in data["Books"].items():
            due_date = datetime.strptime(book_data["return_date"], "%Y-%m-%d")
            if today > due_date:
                print(f"'{book_data['title']}' is OVERDUE! Due date was {book_data['return_date']}.")
            else:
                print(f"'{book_data['title']}' is due on {book_data['return_date']}.")

def empty_cart(self):
        """
        Return all borrowed books (clear cart).
        """
        data = self.get_all_books()
        if len(data["Books"].items()) > 0:
            data = {"Books": {}}

            with open(self.database_path, 'w') as file:
                json.dump(data, file, indent=4)

            self.isEmpty = True
            self.isActive = False
            print("All borrowed books have been returned.")
        else:
            print("No borrowed books to return.")


