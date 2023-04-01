from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, publication_year, edition, authors, price, discount):
        self.title = title
        self.publication_year = publication_year
        self.edition = edition
        self.authors = authors
        self.__price = price
        self.__discount = discount
    
    @abstractmethod ## abstraction
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
    
    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}, Public. Year: {self.publication_year}, Author: {self.edition}, Price: {self.get_price()}"

# Inheritance
class Novel(Book):
    def __init__(self, title, publication_year, edition, authors, price, pages, age): ## -> 3 
        super().__init__(title, publication_year, edition, authors, price) ##  -> 1
        self.pages = pages ## -> 2
        self.age   = age ## -> 2

novel1 = Novel('anna karienina',1870, "3ed", ['Liev Tolstoi'], 70, 1100, "ideology")
print(novel1)


# Polymorphism
class Academic(Book):
    def __init__(self, title, publication_year, edition, authors, price, pages, department): ## -> 3 
        super().__init__(title, publication_year, edition, authors, price) ##  -> 1
        self.pages      = pages ## -> 2
        self.department = department ## -> 2

    ## method repr adapt itself from parent class to child class 
    def __repr__(self):
        return f"Book: {self.title}, Department: {self.department}, Authors: {self.authors}, Pages: {self.pages}, Price: {self.get_price()}"

academic1 = Academic('bitcoin black paper ',2019, "1ed", ['nassim taleb'], 0, 26, "mathematic")
print(academic1)
