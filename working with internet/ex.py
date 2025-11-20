from tkinter import * 
from tkinter import ttk
from urllib.request import urlopen

URL = "http://slashdot.org/slashdot.rss"

class App:
    def __init__(self, root):
        self.root = root
        root.title("RSS reader")

        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="both", expand=True)

        self.listbox = Listbox(frame, width=86, height=20)
        self.listbox.grid(row=0, column=0, sticky="nsew")
        self.listbox.bind("<<ListboxSelect>>", self.show_description)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="nsw")
        self.listbox.configure(yscrollcommand=scrollbar.set)

        self.text = Text(frame, wrap="word")
        self.text.grid(row=0, column=2, sticky="nsew")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(2, weight=1)

        self.items = []
        self.load_rss()

    def extract_from_tag(self, text, tag):
        start_tag = f"<{tag}>"
        end_tag = f"</{tag}>"
        start = text.find(start_tag)
        
        if start == -1:
            return ""
        start += len(start_tag)

        end = text.find(end_tag, start)
        if end == -1:
            return ""
    
        return text[start:end].strip()
    
    def load_rss(self):
        try:
            data = urlopen(URL).read().decode()
            parts = data.split("<item ")
            for part in parts[1:]:
                title = self.extract_from_tag(part, "title")
                description = self.extract_from_tag(part, "description")
                description = self.strip_tags(description)

                self.items.append({
                    "title": title,
                    "description": description
                })

                self.listbox.insert(END, title)
        except Exception as e:
            self.listbox.insert(END, f"Error: {e}")
    
    def show_description(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        
        index = selection[0]
        description = self.items[index]["description"]

        self.text.delete("1.0", END)
        self.text.insert(END, description)

    def strip_tags(self, description):
        cut_pos = description.find("&lt;p&gt;&lt;div") # <p><div
        if cut_pos != -1:
            description = description[:cut_pos]
        return description

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()