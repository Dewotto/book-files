import book

filename = ''

def main():
    book_list = []
    print("Starting the system ...")
    filename = input("Enter book catalog filename: ")
    load_books(book_list, filename)
    print("Book catalog has been loaded.")
    menu_header = """\
Reader's Guild Library - Main Menu
==================================
1. Search for books
2. Borrow a book
3. Return a book
0. Exit the system
    """
    menu_options = {
        1 : True,
        2 : True,
        3 : True,
        2130 : True,
        0 : True
    }
    #this loop collects user input to chose a menu option, and while they choose not to quit, it keeps running
    #it also exits if the user is a library administrator so it can move to the next loop just for admins
    option = print_menu(menu_header, menu_options)
    while option != 0 and option != 2130:
        if option == 1:
            search_books()
        elif option == 2:
            borrow_book(book_list)
        elif option == 3:
            return_book(book_list)
        option = print_menu(menu_header, menu_options)
    #this loop is just for library admins 
    if option == 2130:
        #changes menu header and options to expand the librarians choice of what to do
        menu_header = """\
        Reader's Guild Library - Librarian Menu
        ==================================
        1. Search for books
        2. Borrow a book
        3. Return a book
        4. Add a book
        5. Remove a book
        6. Print catalog
        0. Exit the system
        """
        menu_options = {
            1 : True,
            2 : True,
            3 : True,
            4 : True,
            5 : True,
            6 : True,
            2130 : True,
            0 : True
        }
        option = print_menu(menu_header, menu_options)
        while option != 0:
            if option == 1:
                search_books()
            elif option == 2:
                borrow_book(book_list)
            elif option == 3:
                return_book(book_list)
            elif option == 4:
                add_book()
            elif option == 5:
                remove_book(book_list)



#loads books into a list called 'book_list'
def load_books(book_list, filename):
    file_content = open(filename, 'r')
    for line in file_content:
        raw_line = line.rstrip().split(',')
        if raw_line[4] == "True":
            availability = True
        else:
            availability = False
        book_list.append(book.Book(raw_line[0], raw_line[1], raw_line[2], int(raw_line[3]), availability))
    file_content.close()
    return len(book_list)

#receives variables menu header and menu options to print current menu and also check if choice is valid 
def print_menu(menu_header, menu_options):
    print(menu_header)
    selection = int(input("Enter your selection: "))
    while menu_options[selection] != True:
        print("Invalid option")
        selection = int(input("Enter your selection: "))
    return selection

def search_books():
    pass

def add_book():
    pass

#sets book object status from true to false using the .borrow_it() method from the book.py file
def borrow_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    book_index = find_book_by_isbn(book_list, isbn)
    if book_index != -1:
        if book_list[book_index] == True:
            book_list[book_index].borrow_it()
            print(f"'{book_list[book_index].get_title}' with ISBN {isbn} successfully borrowed.")
        else:
            print(f"'{book_list[book_index].get_title}' with ISBN {isbn} is not currently available.")
    else:
        print("No book found with that ISBN")
    
#removes books from the main book list. DOES NOT REMOVE FROM FILE UNTIL FILE IS SAVED
def remove_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    book_index = find_book_by_isbn(book_list, isbn)
    if book_index != -1:
        book_list.pop(book_index)
        print(f"'{book_list[book_index].get_title}' with ISBN {isbn} successfully removed.")
    else:
        print("No book found with that ISBN")

#Searches though list of books to find if there is a matching isbn. If there is, it returns the list index of that book. If it cant find it it returns negative 1
def find_book_by_isbn(book_list, isbn):
    counter = -1
    for item in book_list:
        current_isbn = item.get_isbn()
        counter += 1
        if isbn == current_isbn:
            return counter

#marks book status as available / true
def return_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    book_index = find_book_by_isbn(book_list, isbn)
    if book_index != -1:
        if book_list[book_index] == False:
            book_list[book_index].return_it()
            print(f"'{book_list[book_index].get_title}' with ISBN {isbn} successfully returned.")
        else:
            print(f"'{book_list[book_index].get_title}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN")
    

if __name__ == "__main__":
    main()