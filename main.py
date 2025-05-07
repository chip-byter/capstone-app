import customtkinter as ctk
from home import Home
from books import Books

class Organicer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organicer")
        self.resizable(False, False)
        self.geometry("700x400")
        # self.geometry("720x480")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.frames = {}

        home_page = Home(self, self)
        self.frames["Home"] = home_page
        home_page.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        books_page = Books(self, self, home_page)
        self.frames["Books"] = books_page
        books_page.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.show_frame("Home")

    def show_frame(self, page_name):
        home_page = self.frames["Home"]
        books_page = self.frames["Books"]
        for each_frame in self.frames.values():
            each_frame.grid_remove()
        if page_name == "Home":
            home_page.search_field.delete(0, ctk.END) 

        if page_name == "Books":
            query = home_page.search_field.get().strip()
            if not query.strip():
                print("Please enter the title or author of the book")
                return
            if not query:
                self.show_frame("Home")
                return
            query = home_page.search_field.get()
            books_page.search_query(query, books_page.results_frame)
        self.frames[page_name].grid(row=0, column=0, sticky="nsew")

        
    




if __name__ == "__main__":
    app = Organicer()
    app.mainloop()