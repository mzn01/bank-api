# 1. The Blueprint for a single Book
class Book:
    def __init__(self, title, author):
        # 'self' means "this specific book I am creating right now"
        self.title = title
        self.author = author

    def __str__(self):
        # This tells Python how to print the book prettily
        return f"'{self.title}' by {self.author}"

# 2. The Blueprint for the Library (which holds Books)
class Library:
    def __init__(self):
        self.books = [] # Start with an empty list

    def add_book(self, book_object):
        self.books.append(book_object)
        print(f"Added: {book_object.title}")

    def remove_book(self, title_to_remove):
        # We have to look through the list to find the match
        # This is a 'List Comprehension' - a pro Python move
        # It keeps all books usually, EXCEPT the one with the matching title
        self.books = [b for b in self.books if b.title != title_to_remove]

    def show_books(self):
        print("--- Library Catalog ---")
        for b in self.books:
            print(b) # This uses the __str__ function from the Book class

# --- USAGE (The "Main" code) ---
# Create the Library
my_lib = Library()

# Create Book Objects
b1 = Book("Atomic Habits", "James Clear")
b2 = Book("Deep Work", "Cal Newport")

# Use the Library
my_lib.add_book(b1)
my_lib.add_book(b2)
my_lib.show_books()

my_lib.remove_book("Atomic Habits")
my_lib.show_books()