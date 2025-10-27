class Item:
    def __init__(self, id: int, title: str, year: int, genre: str, description: str = "", image_path: str = ""):
        self.id = id
        self.title = title
        self.year = year
        self.genre = genre
        self.description = description
        self.image_path = image_path
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}"
    
    def print_data(self):
        return f'Item: {self.title}\nYear: {self.year}\nGenre: {self.genre}\nDescription: {self.description}'
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "description": self.description,
            "image_path": self.image_path,
            "type": "Item"
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            title=data.get("title", ""),
            year=data.get("year", 0),
            genre=data.get("genre", ""),
            description=data.get("description", ""),
            image_path=data.get("image_path", "")
        )

    def print_details(self):
        return f'Type: Item\nID: {self.id}\nTitle: {self.title}\nYear: {self.year}\nGenre: {self.genre}\nDescription: {self.description}'