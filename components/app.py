#!/usr/bin/python3

import customtkinter

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ver = "0.1"
        self.running = False

        self.title("GameAide")
        self.geometry("400x600")

        # configure grid layout (2x6) 4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    def version(self):
        return "version: {}".format(str(self.ver))


    def run(self):
        if self.running == False:
            self.running = True


if __name__ == "__main__":
    app = App()

    app.mainloop()
