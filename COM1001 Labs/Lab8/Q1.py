#Editor Note: You might notice there is no Book class. I didn't use it since it was not necessary at all.
#You can try to make one with Book class yourself. You will see how useless it is. 🤠
#There is a mistake with the fee part of the problem as 
#they stated it should be 50TL yet the output shows it being 2TL per day.
#last line of the output is also incorrect lmao.

class Library():
    def __init__(self, books = {}, users = {}):
        self.books = books
        self.users = users
    
    def borrow_book(self, user, book): #Editor Note: So in the way I did it, the current holder of the book is also contained within the waitlist. Might not be the smartest thing but made this a lot easier to code.
        if len(self.books[book]) == 0: #Checks if anyone currently holds the book at the moment.
            self.users[user] = self.users.get(user, []) + [book]
            self.books[book].append(user)
            print(f"{user} borrowed {book} | waitlist={self.books[book][1:]}")
        else: #If the book is unavailable, it adds the name to the waitlist.
            self.books[book].append(user)
            print(f"{book} unavailable, {user} added to waitlist | waitlist={self.books[book][1:]}")
    
    def list_user_books(self, user):
        if not self.users.get(user, False):
            self.users[user] = []
        return self.users[user]
    
    def return_book(self, user, book, day): #It removes the book from user's dictionary entry and removes the user from book's waitlist.
        self.users[user].remove(book)
        self.books[book].pop(0)
        self.users[self.books[book][0]] += [book]
        print(f"{user} returned {book}, fee={2*(day-14) if day > 14 else 0}, next={self.books[book][0]} | waitlist={self.books[book][1:]}")

lib = Library({"1984":[],"Dune":[]},{})

lib.borrow_book("Alice", "1984")
lib.borrow_book("Bob", "1984")
lib.borrow_book("Charlie", "1984")
lib.borrow_book("Dave", "1984")
lib.borrow_book("Alice", "Dune")
lib.borrow_book("Eve", "Dune")
print(lib.list_user_books("Alice"))
print(lib.list_user_books("Bob"))
print(lib.list_user_books("Charlie"))
print(lib.list_user_books("Dave"))
print(lib.list_user_books("Eve"))
lib.return_book("Alice", "1984", 35)
lib.return_book("Bob", "1984", 22)
lib.return_book("Charlie", "1984", 10)
print(lib.list_user_books("Dave"))