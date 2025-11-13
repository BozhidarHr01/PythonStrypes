from item import Item
class Book(Item):
    def __init__(self, id: int, title: str, year: int, genre: str, author: str, pages: int,  description: str = "", image_path: str = ""):
        super().__init__(id, title, year, genre, description, image_path)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.genre} [{self.pages} pages]"
    
    def print_data(self):
        return f'Book: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nGenre: {self.genre}\nPages: {self.pages}\nDescription: {self.description}'
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "author": self.author,
            "pages": self.pages,
            "type": "Book"
        })
        return data
    
    def get_image_path(self):
        return self.image_path
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            title=data.get("title", ""),
            year=data.get("year", 0),
            genre=data.get("genre", ""),
            author=data.get("author", ""),
            pages=data.get("pages", 0),
            description=data.get("description", ""),
            image_path=data.get("image_path", "")
        )
    
    def print_details(self):
        return f'Type: Book\nID: {self.id}\nTitle: {self.title}\nYear: {self.year}\nGenre: {self.genre}\nAuthor: {self.author}\nPages: {self.pages}\nDescription: {self.description}'