from abc import ABCMeta, abstractstaticmethod
import tkinter as tk

class IUserInterfaceException(Exception):
    pass

class IUserInterface(metaclass=ABCMeta):

    @staticmethod
    def frame():
        """ Interface Method """

    @staticmethod
    def label():
        """ Interface Method """

    @staticmethod
    def build_ui_loop():
        """ Interface Method """

class NewWindow(IUserInterface):
    def __init__(self, relief: tk, bd: int):
        self._window = tk.Tk()
        self._relief = relief
        self._bd = bd

    def frame(self):
        frame = tk.Frame(self._window, relief=self._relief, bd=self._bd)
        frame.grid()
        return self._window

class NewLabel(IUserInterface):
    
    def __init__(self, window: tk, column: int, row: int): 
        self._window = window
        self._column = column
        self._row = row

    def label(self, text: str):
        return tk.Label(self._window, text=text).grid(column=self._column, row=self._row)

class BuildUserInterface(IUserInterface):

    def __init__(self, window: tk):
        self._window = window

    def build_ui_loop(self):
        return self._window.mainloop()

class UserInterfaceFactory:
    
    @staticmethod
    def new_gui(data_type: int, relief: tk, bd: int):
        if (data_type == 0):
            return NewWindow(relief=relief, bd=bd)
        raise IUserInterfaceException("Invalid data type")

    @staticmethod
    def add_item(data_type: int, window: tk, column: int, row: int):
        if (data_type == 0):
            return NewLabel(window=window, column=column, row=row)
    
    @staticmethod
    def build_ui(build: bool, window: tk):
        if (build):
            return BuildUserInterface(window=window)
        if (not build):
            return None
        raise IUserInterfaceException("Invalid datatype in build")