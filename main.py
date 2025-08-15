from library_cart.book import Book
from library_cart.cart import LibraryCart

if __name__ == "__main__":

    # main database path
    database = "./database.json"
    my_cart = LibraryCart(database)

    # search for a book
    print("Searching book...")
    results = my_cart.search_books("Pyhon 101")
    print("--------------------------")

    # get total number of borrowed books
    print("Total books in the current cart:")
    total_book_count = my_cart.get_total_book_count()
    print(f"Total book count: {total_book_count}")
    print("--------------------------")

    # borrow books
    print("Borrowing books...")
    print("--------------------------")
    book001 = Book("Python 101", "Iveelt Batjargal")
    my_cart.borrow_book(book001, days_to_return=14)
    book002 = Book("Data Science", "Eddie")
    my_cart.borrow_book(book002, days_to_return=21)

    # get all borrowed books
    print("--------------------------")
    print("Getting all borrowed books:")
    print("--------------------------")
    my_cart.get_all_books(verbose=1)
    print("--------------------------")

    # remove books by query (title/author)
    print("Returning all books matching a query:")
    print("--------------------------")
    my_cart.return_book_by_query("Python 101")
    print("--------------------------\n")

    # check due dates for remaining books
    print("Checking due dates for borrowed books:")
    print("--------------------------")
    my_cart.check_due_dates()
    print("--------------------------")

    # get updated list
    print("All current borrowed books:")
    my_cart.get_all_books(verbose=1)
    print("--------------------------")

    # empty cart
    print("Returning all books (empty cart):")
    my_cart.empty_cart()
    print("--------------------------")

