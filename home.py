import customtkinter as ctk

class Home(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # self.font_title = ctk.CTkFont(family="Courier New", size=100, weight="bold")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.app_name = ctk.CTkLabel(self, text="ORGANICER", font=("Courier New", 80, "bold"))
        self.app_name.grid(row=0, column=0, columnspan=2, sticky="s")
        
        self.transactions = ctk.CTkFrame(self, fg_color="transparent")
        self.transactions.grid(row=1, column=0, sticky="n")

        self.search_field = ctk.CTkEntry(self.transactions)
        self.search_field.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="new")
        self.search_field.bind("<Map>", self.search_field_focus)
        self.search_field.bind("<Return>", lambda event: controller.show_frame("Books"))

        self.search_btn = ctk.CTkButton(self.transactions, text="Search", command=lambda: controller.show_frame("Books"))
        self.search_btn.grid(row=0, column=2, padx=5, pady=5, sticky="nw")

        self.lend_btn = ctk.CTkButton(self.transactions, text="Lend a Book", command=lambda: controller.scan_frame("Lending", 5000))
        self.lend_btn.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        self.return_btn = ctk.CTkButton(self.transactions, text="Return a Book", command=lambda: controller.scan_frame("Returning", 5000))
        self.return_btn.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        self.add_btn = ctk.CTkButton(self.transactions, text="Add a Book")
        self.add_btn.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        
    def search_field_focus(self, event):
        self.search_field.focus_set()