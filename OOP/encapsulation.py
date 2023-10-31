class Author:
    def __init__(self, birth_year: int, name: str) -> None:
        self.birth_year = birth_year
        self.name = name
    
    def get_author_info(self):
        return f"{self.name} born in {self.birth_year}"
    
class Book:
    def __init__(self, title: str, pub_year: str, author: Author) -> None:
        self.title = title
        self.pub_year = pub_year
        self.author = author

    def get_book_info(self):
        return f"{self.title} belongs to {self.author.get_author_info()}, published in {self.pub_year}"
    
if __name__ == "__main__":
    author  = Author(birth_year=1994, name="Edward Leo Gate")
    book = Book(title="vitamin gau gau", pub_year="2013", author=author)
    print(book.get_book_info())