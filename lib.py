class Library:
    def _init_(self):
        self.books = []  # List to store books as tuples (book_name, author, book_number)
        self.borrowed_books = {}  # Dictionary to track borrowed books by user
        self.admin_username = "admin"
        self.admin_password = "admin123"
        self.users = {"user1": "password1", "user2": "password2"}  # Sample users

    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == self.admin_username and password == self.admin_password:
            self.admin_menu()
        else:
            print("Invalid admin credentials.")

    def user_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users and self.users[username] == password:
            self.user_menu(username)
        else:
            print("Invalid user credentials.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Book")
            print("2. Delete Book")
            print("3. Show All Books")
            print("4. Exit to Login")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.show_books()
            elif choice == "4":
                print("Exiting admin menu...")
                break
            else:
                print("Invalid option. Please try again.")

    def user_menu(self, username):
        while True:
            print("\nUser Menu:")
            print("1. Show Books Taken by User")
            print("2. Return Book")
            print("3. Exit to Login")
            choice = input("Choose an option: ")

            if choice == "1":
                self.show_user_books(username)
            elif choice == "2":
                self.return_book(username)
            elif choice == "3":
                print("Exiting user menu...")
                break
            else:
                print("Invalid option. Please try again.")

    def add_book(self):
        book_name = input("Enter book name: ")
        author_name = input("Enter author name: ")
        book_number = input("Enter book number: ")
        self.books.append((book_name, author_name, book_number))
        print(f"Book '{book_name}' by '{author_name}' added.")

    def delete_book(self):
        book_name = input("Enter the name of the book to delete: ")
        for book in self.books:
            if book[0] == book_name:
                self.books.remove(book)
                print(f"Book '{book_name}' has been deleted.")
                return
        print(f"Book '{book_name}' not found.")

    def show_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- Name: {book[0]}, Author: {book[1]}, Number: {book[2]}")

    def show_user_books(self, username):
        if username in self.borrowed_books and self.borrowed_books[username]:
            print(f"{username} has borrowed the following books:")
            for book in self.borrowed_books[username]:
                print(f"- {book}")
        else:
            print(f"{username} has not borrowed any books.")

    def return_book(self, username):
        if username in self.borrowed_books:
            book_to_return = input("Enter the name of the book to return: ")
            if book_to_return in self.borrowed_books[username]:
                self.borrowed_books[username].remove(book_to_return)
                self.books.append((book_to_return, "Unknown", "Unknown"))  # Add back to library
                print(f"Book '{book_to_return}' has been returned.")
            else:
                print(f"{username} has not borrowed the book '{book_to_return}'.")
        else:
            print(f"{username} has not borrowed any books.")

    def start(self):
        while True:
            print("\nWelcome to the Library System!")
            print("1. Admin Login")
            print("2. User Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.admin_login()
            elif choice == "2":
                self.user_login()
            elif choice == "3":
                print("Exiting the library system...")
                break
            else:
                print("Invalid option. Please try again.")


# Run the library system
library = Library()
library.start()
