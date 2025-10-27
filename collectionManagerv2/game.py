from item import Item
class Game(Item):
    def __init__(self, id: int, title: str, year: int, genre: str, platform: str, developer: str, description: str = "", image_path: str = ""):
        super().__init__(id, title, year, genre, description, image_path)
        self.platform = platform
        self.developer = developer

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre} on {self.platform}, developed by {self.developer}"
    
    def print_data(self):
        return f'Game: {self.title}\nDeveloper: {self.developer}\nPlatform: {self.platform}\nYear: {self.year}\nGenre: {self.genre}\nDescription: {self.description}'
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "platform": self.platform,
            "developer": self.developer,
            "type": "Game"
        })
        return data
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            title=data.get("title", ""),
            year=data.get("year", 0),
            genre=data.get("genre", ""),
            platform=data.get("platform", ""),
            developer=data.get("developer", ""),
            description=data.get("description", ""),
            image_path=data.get("image_path", "")
        )
    
    def print_details(self):
        return f'Type: Game\nID: {self.id}\nTitle: {self.title}\nYear: {self.year}\nGenre: {self.genre}\nPlatform: {self.platform}\nDeveloper: {self.developer}\nDescription: {self.description}'