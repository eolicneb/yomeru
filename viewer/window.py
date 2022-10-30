import tkinter as tk


class Label(tk.Label):
    def insert(self, _, text):
        self.config(text=text)


class Character(tk.Frame):
    backgrounds = ["white", "gray"]
    creation_index = 0

    def __init__(self, symbol, root, kao_font=None, onsei_font=None,
                 **kwargs):
        self.kao = symbol.kao
        self.onsei = symbol.onsei
        self.kao_entry = None
        self.onsei_entry = None
        kwargs.pop("bg", None)
        self.kao_font = kao_font
        self.onsei_font = onsei_font
        super().__init__(root, **kwargs)
        self.index = self.creation_index
        self.increase_creation_index()

    @classmethod
    def increase_creation_index(cls):
        cls.creation_index += 1

    def build_up(self):
        self.grid(rowspan=2, sticky="N")

        self.onsei_entry = Label(self, font=self.onsei_font)
        self.onsei_entry.grid(row=0)
        self.onsei_entry.insert(tk.END, self.onsei)

        self.kao_entry = Label(self, font=self.kao_font)
        self.kao_entry.grid(row=1, sticky="EW")
        self.kao_entry.insert(tk.END, self.kao)
        self.kao_entry.config(bg=self.backgrounds[self.index % len(self.backgrounds)])

    def config(self, *args, **kwargs):
        kwargs.pop("bg", None)
        super().config(*args, **kwargs)

    def set_background(self, *args):
        pass


class Translation(tk.Frame):
    character_class = Character
    backgrounds = ["white", "gray"]

    def __new__(cls, content, root, imi_font=None, **kwargs):
        if hasattr(content, "_uchiryuu"):
            return super().__new__(cls)
        return cls.character_class(content, root, **kwargs)

    def __init__(self, tsubu, root,
                 imi_font=None, kao_font=None, onsei_font=None,
                 **kwargs):
        self.tsubu = tsubu
        self.frames = []
        self.imi_entry = None
        self.imi_font = imi_font
        self.char_font = {"kao_font": kao_font, "onsei_font": onsei_font}
        kwargs.pop("bg", None)
        self.kwargs = kwargs
        self.font = kwargs.pop("font", None)
        super().__init__(root, **kwargs)

    def build_up(self):
        self.grid(sticky="N")

        pos = 0
        for char_index, char in enumerate(self.tsubu._uchiryuu):
            frame = Translation(char, self, imi_font=self.imi_font,
                                **self.char_font, **self.kwargs)
            frame.grid(row=0, column=pos)
            frame.build_up()
            frame.set_background(char_index)
            pos += len(char)
            self.frames.append(frame)

        max_rowspan = max(frame.grid_size()[1] for frame in self.frames)

        self.imi_entry = Label(self, font=self.imi_font)
        self.imi_entry.grid(row=max_rowspan, columnspan=pos)
        self.imi_entry.insert(tk.END, self.tsubu.imi)

    def set_background(self, index):
        background = self.backgrounds[index % len(self.backgrounds)]
        if self.imi_entry:
            self.imi_entry.config(bg=background)
        super().config(bg=background)


class MainWindow(tk.Tk):
    def __init__(self, sentences: list, **kwargs):
        super().__init__()
        self.sentences = sentences
        self.frames = []
        self.containers = []
        self.kwargs = kwargs
        self.kwargs.pop("bg", None)
        self.build_up()

    def build_up(self):
        for row, content in enumerate(self.sentences):
            frame = Translation(content, self, **self.kwargs)
            frame.build_up()
            frame.grid(row=row, sticky="W")
            self.frames.append(frame)


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
