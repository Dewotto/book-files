class Book:
    GENRES = ["Romance",
    "Mystery",
    "Science Fiction",
    "Thriller",
    "Young Adult",
    "Children’s Fiction",
    "Self-help",
    "Fantasy",
    "Historical Fiction",
    "Poetry"]

    


    def __init__(self, isbn, title, author, genre_name, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre_name = genre_name
        self.__available = available

    def get_genre(self):
        return self.__genre_name 
    
    def get_isbn(self):
        return self.__isbn
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre_name(self):
        return Book.GENRES[self.__genre_name]

    def get_availability(self):
        if self.__available:
            return "Available"
        else:
            return "Borrowed"

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
    
    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author

    def set_genre(self, new_genre_name):
        self.__genre_name = new_genre_name

    def borrow_it(self):
        if self.__available:
            self.__available = False

    
    def return_it(self):
        if self.__available == False:
            self.__available = True

    def __str__(self):
        return f"{self.__isbn:<15}{self.__title:<26}{self.__author:<26}{Book.GENRES[self.__genre_name]:<21}{self.get_availability():<15}"
        if self.__available:
            self.__available = False

    
    def return_it(self):
        if self.__available == False:
            self.__available = True

    def __str__(self):
        return f"{self.__isbn:<15}{self.__title:<26}{self.__author:<26}{Book.GENRES[self.__genre_name]:<21}{self.get_availability():<15}"
