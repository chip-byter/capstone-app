import customtkinter as ctk

class Lending(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label_heading = ctk.CTkLabel(self, text="Please scan the library card", font=("Helvetica", 20, "bold"))
        self.label_heading.grid(row=0, column=0, columnspan=2, sticky="s")
        
        self.label_subheading = ctk.CTkLabel(self, text="Scanning...", font=("Helvetica", 13, "italic"))
        self.label_subheading.grid(row=1, column=0, sticky="n")

       
        


class Returning(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label_heading = ctk.CTkLabel(self, text="Please scan the library card", font=("Helvetica", 20, "bold"))
        self.label_heading.grid(row=0, column=0, columnspan=2, sticky="s")
        
        self.label_subheading = ctk.CTkLabel(self, text="Scanning...", font=("Helvetica", 13, "italic"))
        self.label_subheading.grid(row=1, column=0, sticky="n")

     
