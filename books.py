import customtkinter as ctk

class Books(ctk.CTkFrame):
    def __init__(self, parent, controller, home):
        super().__init__(parent)
        
        # self.title("Organicer")
        # self.geometry("700x400")
        
        self.controller = controller
        self.home = home
        # database here


        # self.configure(fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=0)
        self.header_frame.grid_columnconfigure(2, weight=1)

        self.search_field = ctk.CTkEntry(self.header_frame)
        self.search_field.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="new")

        self.search_btn = ctk.CTkButton(self.header_frame, text="Search")
        self.search_btn.grid(row=0, column=2, padx=5, pady=5, sticky="nw")
        
        self.home_btn = ctk.CTkButton(self.header_frame, text="Home", command=lambda: controller.show_frame("Home"))
        self.home_btn.grid(row=0, column=3, sticky="e")


        self.results_frame = ctk.CTkScrollableFrame(self)
        self.results_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def query(self, q):
        self.search_field.delete(0, ctk.END)
        self.search_field.insert(0, q)

        if not q.strip():
            return
        else:
            print(q)

if __name__ == "__main__":
    app = Books()
    app.mainloop()