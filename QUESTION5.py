#(i)
class Book(): 
    def _init_(self,title, author, pages):
         self.title = title
         self.author = author
         self.pages = pages 
    def about_the_book(self): 
         print(f" The tile is{self.title} and the author is{self.author} and the pages are {self.pages}")
Book1 = Book(title =' the journey to the south' ,author="leticia", pages=33)
print(Book1.about_the_book())
#ii)
class Ebook(Book): 
    def _init_(self, title,author, pages ,format):
         self.title = title
         self.author = author
         self.pages = pages
         self.format= format
    def display_information(self):
         print(f" the title is{self.title} and the author is{self.author} and the pages are{self.pages} with the {self.format}")  
 #ii)
class Book():
     Book1 = Book(title =' the journey to the south' ,author="leticia", pages=33)
     Book.pop('pages')
    
                
#class :  these are operators that define the behave of the functions
# object : an object is an atrribute that are found within the class      