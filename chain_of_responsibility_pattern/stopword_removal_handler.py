# stopword_removal_handler.py
from text_cleaning_handler import TextCleaningHandler
from nltk.corpus import stopwords

class StopwordRemovalHandler(TextCleaningHandler):
    def __init__(self):
        super().__init__()
        self.stopwords = set(stopwords.words('english'))

    def handle(self, text):
        text = ' '.join([word for word in text.split() if word not in self.stopwords])
        return super().handle(text)