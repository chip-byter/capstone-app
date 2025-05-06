import customtkinter as ctk
from home import Home

class Organicer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organicer")
        self.geometry("700x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.frames = {}

        self.home_page = Home(self)
        # self.frames["Home"] = self.home
        self.home_page.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # self.show_frame("Home")

    # def show_frame(self, page_name):
    #     for each_frame in self.frames.values():
    #         each_frame.grid_remove()

    #     if page_name == "Books":
    #         home_page = self.frames["Home"]
    #         books_page = self.frames["Books"]
    #         query = home_page.search_field.get().strip()
    #         if not query:
    #             self.show_frame("Home")
    #             return
    #         query = home_page.search_field.get()
    #         books_page.query(query)

if __name__ == "__main__":
    app = Organicer()
    app.mainloop()