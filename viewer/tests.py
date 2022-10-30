import pytest
from viewer.window import MainWindow, Character
from text import p1, p2, p3


def test():
    chars = [p1.honbun, p2.honbun, p3.honbun]
    main = MainWindow(chars, imi_font=('Roboto', 14),
                      onsei_font=('Roboto', 14), kao_font=('Roboto', 16))
    main.mainloop()
    assert True
