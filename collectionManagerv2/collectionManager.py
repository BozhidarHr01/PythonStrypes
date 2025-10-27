from tkinter import *
from book import Book
from movie import Movie
from game import Game
from item import Item

file_path = 'collectionManagerv2/collections.txt'

class CollectionManager():
    def __init__(self):
        self.items = []

    def get_collections(self):
        return self.items
    
    def get_item_details(self, item_name: str):
        for item in self.items:
            if item.title == item_name:
                return item.print_details()
        return None
    
    def add_item(self, item):
        self.items.append(item)
        self.save_collections()
    
    def remove_selected_item(self, item: Item):
        self.items = [it for it in self.items if it.title != item.title]
        self.save_collections()

    def update_item(self, item_id, updated_item):
        for idx, item in enumerate(self.items):
            if item.id == item_id:
                self.items[idx] = updated_item
                return True
        return False
    
    def search_items(self, query):
        query = query.lower()
        return [item for item in self.items if query in item.title.lower()]

    def save_collections(self):
        with open(file_path, 'w') as file:
            for item in self.items:
                data = item.to_dict()
                parts = []
                for k, v in data.items():
                    parts.append(f"{k}={v}")
                line = f"{item.__class__.__name__.lower()}|{' ;'.join(parts)}\n"
                file.write(line)
        
    def load_collections(self):
        self.items.clear()
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    item_type, data_str = line.split('|', 1)
                    data_parts = data_str.split(' ;')
                    data = {}
                    for part in data_parts:
                        key, value = part.split('=', 1)
                        data[key] = value
                    if item_type == 'book':
                        item = Book.from_dict(data)
                    elif item_type == 'movie':
                        item = Movie.from_dict(data)
                    elif item_type == 'game':
                        item = Game.from_dict(data)
                    else:
                        item = Item.from_dict(data)
                    self.items.append(item)
        except FileNotFoundError:
            pass

    def refresh_collections(self):      
        self.items.clear()
        self.load_collections()

    def refresh_collections_file(self):
        self.load_collections()
        self.save_collections()