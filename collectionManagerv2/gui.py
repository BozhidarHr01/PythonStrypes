from tkinter import *
from tkinter import ttk
from item import Item
from game import Game
from movie import Movie
from book import Book
from PIL import Image, ImageTk

from collectionManager import CollectionManager

class CollectionManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Collection Manager")
        self.collection_manager = CollectionManager()
        # self.collection_manager.add_sample_items()
        self.setup_ui()
    
    def setup_ui(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Add Item", command=self.add_collection)
        file_menu.add_command(label="Save", command=self.collection_manager.save_collections)
        file_menu.add_command(label="Exit", command=self.root.quit)

        self.collections_frame = ttk.Frame(self.root, padding="10")

        self.collection_buttons_frame = ttk.Frame(self.collections_frame, padding="5")
        self.collection_buttons_frame.grid(row=0, column=0, sticky=(N, S, E, W))

        books_icon=PhotoImage(file="assets/button_icons/book.png").subsample(15, 15)
        label_books=Label(image=books_icon)
        label_books.image=books_icon
        movies_icon=PhotoImage(file="assets/button_icons/movie.png").subsample(15, 15)
        label_movies=Label(image=movies_icon)
        label_movies.image=movies_icon
        games_icon=PhotoImage(file="assets/button_icons/game.png").subsample(15, 15)
        label_games=Label(image=games_icon)
        label_games.image=games_icon
        all_icon=PhotoImage(file="assets/button_icons/all_items.png").subsample(15, 15)
        label_all=Label(image=all_icon)
        label_all.image=all_icon

        self.show_all = ttk.Button(self.collection_buttons_frame, text="All", image=label_all.image, compound=LEFT, command=self.load_collections)
        self.show_all.grid(row=0, column=0, padx=5, pady=5)
        self.show_books = ttk.Button(self.collection_buttons_frame, text="Books", image=label_books.image, compound=LEFT, command=lambda: self.filter_collections("Book"))
        self.show_books.grid(row=0, column=1, padx=5, pady=5)
        self.show_movies = ttk.Button(self.collection_buttons_frame, text="Movies", image=label_movies.image, compound=LEFT, command=lambda: self.filter_collections("Movie"))
        self.show_movies.grid(row=0, column=2, padx=5, pady=5)
        self.show_games = ttk.Button(self.collection_buttons_frame, text="Games", image=label_games.image, compound=LEFT, command=lambda: self.filter_collections("Game"))
        self.show_games.grid(row=0, column=3, padx=5, pady=5)

        self.collections_frame.grid(row=1, column=0, sticky=(N, S, E, W))
        self.collections_listbox = Listbox(self.collections_frame, height=15, width=50)
        self.collections_listbox.grid(row=1, column=0, sticky=(N, S, E, W))
        scrollbar = Scrollbar(self.collections_frame, orient=VERTICAL, command=self.collections_listbox.yview)
        scrollbar.grid(row=1, column=1, sticky=(N, S))
        self.collections_listbox.config(yscrollcommand=scrollbar.set)

        self.items_count_label = ttk.Label(self.collections_frame, text=f"Items Count: {self.collections_listbox.size()}")
        self.items_count_label.grid(row=2, column=0, sticky=(W, E))

        def focus_in(_):
            if self.search_entry.get() == "Search...":
                self.search_entry.delete(0, END)

        def focus_out(_):
            if not self.search_entry.get():
                self.search_entry.insert(0, "Search...")
                self.refresh_listbox()

        self.search_var = StringVar()
        self.search_entry = Entry(self.collections_frame, textvariable=self.search_var, width=30)
        self.search_entry.grid(row=3, column=0, padx=5, pady=5, sticky=(W, E))

        self.search_entry.insert(0, "Search...")
        self.search_entry.bind("<FocusIn>", focus_in)
        self.search_entry.bind("<FocusOut>", focus_out)

        def on_search_change(*args):
            query = self.search_var.get().strip()
            if query == "Search..." or not query:
                self.refresh_listbox()
            else:
                filtered_items = self.collection_manager.search_items(query)
                self.collections_listbox.delete(0, END)
                for item in filtered_items:
                    self.collections_listbox.insert(END, item.title)
                self.update_items_count()
        self.search_var.trace_add('write', on_search_change)

        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.collections_frame.columnconfigure(1, weight=1)
        self.collections_frame.rowconfigure(1, weight=1)
        
        self.details_frame = ttk.Frame(self.root, padding="10")
        self.details_frame.grid(row=1, column=1, sticky=(N, S, E, W))
        self.details_text = Text(self.details_frame, height=20, width=50, state="disabled")
        self.details_text.grid(row=0, column=0, sticky=(N, S, E, W))

        # self.details_frame.columnconfigure(1, weight=1)
        # self.details_frame.rowconfigure(2, weight=1)

        self.collections_listbox.bind('<<ListboxSelect>>', self.show_details)

        self.buttons_frame = ttk.Frame(self.root, padding="10")
        self.buttons_frame.grid(row=2, column=0, columnspan=2, sticky=(E, W))

        self.image_frame = ttk.Frame(self.root, padding = "10")
        self.image_frame.grid(row = 1, column=2, columnspan=2, sticky=(N, S, E, W))

        add_button_icon=PhotoImage(file="assets/button_icons/add_item.png").subsample(15, 15)
        label_add_button=Label(image=add_button_icon)
        label_add_button.image=add_button_icon
        refresh_button_icon=PhotoImage(file="assets/button_icons/refresh.png").subsample(15, 15)
        label_refresh_button=Label(image=refresh_button_icon)
        label_refresh_button.image=refresh_button_icon
        delete_button_icon=PhotoImage(file="assets/button_icons/remove_item.png").subsample(15, 15)
        label_delete_button=Label(image=delete_button_icon)
        label_delete_button.image=delete_button_icon

        add_button = ttk.Button(self.buttons_frame, text="Add", image=add_button_icon, command=self.add_collection)
        add_button.grid(row=2, column=0, padx=20, pady=10)

        refresh_button = ttk.Button(self.buttons_frame, text="Refresh", image=refresh_button_icon, command=self.refresh_collections)
        refresh_button.grid(row=2, column=1, padx=20, pady=10)

        delete_button = ttk.Button(self.buttons_frame, text="Delete", image=delete_button_icon, command=self.delete_collection)
        delete_button.grid(row=2, column=2, padx=20, pady=10)

        self.collection_manager.load_collections() 
        self.load_collections()

    def filter_collections(self, collection_type):
        self.collections_listbox.delete(0, END)
        filtered_items = [item for item in self.collection_manager.items if item.__class__.__name__ == collection_type]
        for item in filtered_items:
            self.collections_listbox.insert(END, item.title)

    def update_items_count(self):
        count = self.collections_listbox.size()
        self.items_count_label.config(text=f"Items Count: {count}")

    def show_details(self, _):
        selected_item = self.collections_listbox.curselection()
        if selected_item:
            collection_name = self.collections_listbox.get(selected_item)
            self.details_text.config(state="normal")
            self.details_text.delete(1.0, END)
            self.details_text.insert(END, f"Details for {collection_name}")
            
            item = self.collection_manager.get_item_details(collection_name)
            
            self.details_text.insert(END, f"\n\n{item}")
            self.details_text.config(state="disabled")

            image_path = self.collection_manager.get_image_path_for_item(collection_name)
            if image_path:
                image = Image.open(image_path)
                resized_image = image.resize((150, 195))
                img = ImageTk.PhotoImage(resized_image)
                label = Label(self.image_frame, image=img)
                label.grid(row=1, column=1, sticky=(N, S, E, W))
                self.image_frame.columnconfigure(1,weight=1)
                self.image_frame.rowconfigure(1,weight=1)
                label.image = img
            else:
                label.image = None

    def load_collections(self):
        self.collections_listbox.delete(0, END)
        collections = self.collection_manager.get_collections()
        for item in collections:
            self.collections_listbox.insert(END, item.title)
        self.update_items_count()

    def add_collection(self):
        self.open_add_window() 
        self.collection_manager.save_collections()

    def update_add_window(self, selected_type):
        self.selected_type = selected_type
        self.type_entry.set(selected_type)
        for widget in self.add_window.winfo_children():
            widget.destroy()
        self.create_add_window_fields()

    def create_add_window_fields(self):
        self.type_entry = StringVar()
        
        ttk.Label(self.add_window, text="Title:").grid(row=1, column=0, padx=10, pady=10)
        self.title_entry = ttk.Entry(self.add_window)
        self.title_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.add_window, text="Year:").grid(row=2, column=0, padx=10, pady=10)
        self.year_entry = ttk.Entry(self.add_window)
        self.year_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.add_window, text="Genre:").grid(row=3, column=0, padx=10, pady=10)
        self.genre_entry = ttk.Entry(self.add_window)
        self.genre_entry.grid(row=3, column=1, padx=10, pady=10)

        if self.selected_type == "Book":
            self.type_entry.set("Book")
            ttk.Label(self.add_window, text="Author:").grid(row=4, column=0, padx=10, pady=10)
            self.author_entry = ttk.Entry(self.add_window)
            self.author_entry.grid(row=4, column=1, padx=10, pady=10)
            ttk.Label(self.add_window, text="Pages:").grid(row=5, column=0, padx=10, pady=10)
            self.pages_entry = ttk.Entry(self.add_window)
            self.pages_entry.grid(row=5, column=1, padx=10, pady=10)
        elif self.selected_type == "Movie":
            self.type_entry.set("Movie")
            ttk.Label(self.add_window, text="Director:").grid(row=4, column=0, padx=10, pady=10)
            self.director_entry = ttk.Entry(self.add_window)
            self.director_entry.grid(row=4, column=1, padx=10, pady=10)
            ttk.Label(self.add_window, text="Duration (min):").grid(row=5, column=0, padx=10, pady=10)
            self.duration_entry = ttk.Entry(self.add_window)
            self.duration_entry.grid(row=5, column=1, padx=10, pady=10)
        elif self.selected_type == "Game":
            self.type_entry.set("Game")
            ttk.Label(self.add_window, text="Developer:").grid(row=4, column=0, padx=10, pady=10)
            self.developer_entry = ttk.Entry(self.add_window)
            self.developer_entry.grid(row=4, column=1, padx=10, pady=10)
            ttk.Label(self.add_window, text="Platform:").grid(row=5, column=0, padx=10, pady=10)
            self.platform_entry = ttk.Entry(self.add_window)
            self.platform_entry.grid(row=5, column=1, padx=10, pady=10)

        self.optionMenu = ttk.OptionMenu(self.add_window, self.type_entry, self.type_entry.get(), "Book", "Movie", "Game", command=self.update_add_window)
        self.optionMenu.grid(row=0, column=1, padx=10, pady=10)

        def save_new_collection():
            title = self.title_entry.get()
            year = int(self.year_entry.get())
            genre = self.genre_entry.get()
            if self.selected_type == "Book":
                author = self.author_entry.get()
                pages = int(self.pages_entry.get())
                new_item = Book(id=len(self.collection_manager.items)+1, title=title, year=year, genre=genre, author=author, pages=pages)
            elif self.selected_type == "Movie":
                director = self.director_entry.get()
                duration = int(self.duration_entry.get())
                new_item = Movie(id=len(self.collection_manager.items)+1, title=title, year=year, genre=genre, director=director, duration=duration)
            elif self.selected_type == "Game":
                developer = self.developer_entry.get()
                platform = self.platform_entry.get()
                new_item = Game(id=len(self.collection_manager.items)+1, title=title, year=year, genre=genre, developer=developer, platform=platform)
            self.collection_manager.add_item(new_item)
            self.load_collections()
            self.add_window.destroy()

        save_button = ttk.Button(self.add_window, text="Save", command=save_new_collection)

        save_button.grid(row=6, column=0, columnspan=2, pady=10)

    def open_add_window(self):
        self.add_window = Toplevel(self.root)
        self.add_window.title("Add New Collection")
        self.add_window.transient(self.root)
        
        self.selected_type = "Book"
        self.create_add_window_fields()

    def delete_collection(self):
        selected_item = self.collections_listbox.curselection()
        if selected_item:
            collection_name = self.collections_listbox.get(selected_item)
            if collection_name:
                item_to_delete = None
                for item in self.collection_manager.items:
                    if item.title == collection_name:
                        item_to_delete = item
                        break
                if item_to_delete:
                    self.collection_manager.remove_selected_item(item_to_delete)
                    self.load_collections()
                    self.details_text.config(state="normal")
                    self.details_text.delete(1.0, END)
                    self.details_text.insert(END, f"Deleted collection: {collection_name}")
                    self.details_text.config(state="disabled")

    def refresh_collections(self):
        self.load_collections()
        self.update_items_count()

if __name__ == "__main__":
    root = Tk()
    app = CollectionManagerGUI(root)
    root.mainloop()