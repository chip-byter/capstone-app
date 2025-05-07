import customtkinter as ctk
from database import Database
from PIL import Image


class Books(ctk.CTkFrame):
    def __init__(self, parent, controller, home):
        super().__init__(parent)
        
        self.controller = controller
        self.home = home

        self.db = Database()
        # self.configure(fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, pady=10, sticky="ew")
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=0)
        self.header_frame.grid_columnconfigure(2, weight=1)

        self.search_field = ctk.CTkEntry(self.header_frame)
        self.search_field.grid(row=0, column=0, padx=(0, 5), pady=5, columnspan=2, sticky="new")
        
      
        self.search_btn = ctk.CTkButton(self.header_frame, text="Search",  command=lambda: self.search_query(self.search_field.get(), self.results_frame))
        self.search_btn.grid(row=0, column=2, padx=5, pady=5, sticky="nw")
        
        self.home_btn = ctk.CTkButton(self.header_frame, text="Home", width=70, command=lambda: controller.show_frame("Home"))
        self.home_btn.grid(row=0, column=3, sticky="e")


        self.results_frame = ctk.CTkScrollableFrame(self)
        self.results_frame.grid(row=1, column=0, pady=(10, 0), sticky="nsew")
        

    def search_query(self, q: str, target_frame):
        self.search_field.delete(0, ctk.END)
        self.search_field.insert(0, q)

        for widget in target_frame.winfo_children():
            widget.destroy()

        self.db.cursor.execute("SELECT title, author FROM books_table WHERE title LIKE ? OR author LIKE ?", ("%" + q + "%", "%" + q + "%"))
        results = self.db.cursor.fetchall()

        if len(results) == 0:
            self.results_frame.grid_remove()
            self.no_result = ctk.CTkFrame(self)
            self.no_result.grid(row=1, column=0, pady=(10, 0), sticky="nsew")
            self.no_result.grid_columnconfigure(0, weight=1)
            self.no_result.grid_rowconfigure(0, weight=1)
            self.no_result.grid_rowconfigure(1, weight=1)

            self.message = ctk.CTkLabel(self.no_result, text=f"Sorry, there's no result for '{q}'.", font=("Helvetica", 20, "bold"))
            self.message.grid(row=0, column=0, sticky="sew")
            self.sub_message = ctk.CTkLabel(self.no_result, text=f"Please check your spelling or enter a specific book title or author.", font=("Helvetica", 13, "italic"))
            self.sub_message.grid(row=1, column=0, sticky="new")
            
        else:
            target_frame.grid()
            self.no_result.grid_remove()
            col = 0
            row = 0
            
            for title, author in results:
                self.book_card = BookCard(target_frame, title, author, "images/the_catcher_in_the_rye_cover.jpg")
                self.book_card.grid(row=row, column=col, pady=(0, 10), padx=(0, 10), sticky="w")
                col+= 1
                if col >= 4:  
                    col = 0
                    row += 1

class BookCard(ctk.CTkFrame):
    def __init__(self, parent, book_title:str, author:str, path:str):
    # def __init__(self, parent):
        super().__init__(parent)
        self.title = book_title
        self.author = author
        self.path = path

        self.image = ctk.CTkImage(dark_image=Image.open(self.path), size=(145, 217))
        self.book_cover = ctk.CTkLabel(self, text="", image=self.image)
        self.book_cover.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.book_metadata = ctk.CTkFrame(self, fg_color="transparent")
        self.book_metadata.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="nsew")
        self.book_metadata.grid_columnconfigure(0, weight=1)

        self.book_title = ctk.CTkLabel(self.book_metadata, text=self.title, wraplength=130, font=("helvetica", 12, "bold"), justify="center")
        
        self.book_title.grid(row=0, column=0, sticky="nsew")

        self.book_author = ctk.CTkLabel(self.book_metadata, text=self.author)
        self.book_author.grid(row=1, column=0, sticky="nsew")



        

if __name__ == "__main__":
    app = Books()
    app.mainloop()