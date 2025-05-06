import customtkinter as ctk

class Organicer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organicer")
        self.geometry("700x400")
        
        self.frames = {}




    # def show_frame(self, page_name):
    #     for each_frame in self.frames.values():
    #         each_frame.grid_remove()

if __name__ == "__main__":
    app = Organicer()
    app.mainloop()