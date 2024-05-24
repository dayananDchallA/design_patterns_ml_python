# text_cleaning_handler.py
from abc import ABC, abstractmethod

class TextCleaningHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, text):
        if self.next_handler:
            return self.next_handler.handle(text)
        return text
