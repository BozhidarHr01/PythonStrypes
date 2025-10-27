from item import Item
class Movie(Item):
    def __init__(self, id: int, title: str, year: int, genre: str, director: str, duration: int = 0, description: str = "", image_path: str = ""):
            super().__init__(id, title, year, genre, description, image_path)
            self.director = director
            self.duration = duration
    
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.director}'
    
    def print_data(self):
        return f'Movie: {self.title}\nDirector: {self.director}\nYear: {self.year}\nGenre: {self.genre}\nDuration: {self.duration} mins \nDescription: {self.description}'
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "director": self.director,
            "duration": self.duration,
            "type": "Movie"
        })
        return data 
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            title=data.get("title", ""),
            year=data.get("year", 0),
            genre=data.get("genre", ""),
            director=data.get("director", ""),
            duration=data.get("duration", 0),
            description=data.get("description", ""),
            image_path=data.get("image_path", "")
        )
    
    def print_details(self):
        return f'Type: Movie\nID: {self.id}\nTitle: {self.title}\nYear: {self.year}\nGenre: {self.genre}\nDirector: {self.director}\nDuration: {self.duration} mins\nDescription: {self.description}'