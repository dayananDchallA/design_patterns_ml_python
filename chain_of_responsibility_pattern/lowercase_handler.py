# lowercase_handler.py
import re
from text_cleaning_handler import TextCleaningHandler

class LowercaseHandler(TextCleaningHandler):
    def handle(self, text):
        text = text.lower()
        return super().handle(text)

