# setup_chain.py
from lowercase_handler import LowercaseHandler
from punctuation_removal_handler import PunctuationRemovalHandler
from stopword_removal_handler import StopwordRemovalHandler

def setup_chain():
    # Create handlers
    lowercase_handler = LowercaseHandler()
    punctuation_removal_handler = PunctuationRemovalHandler()
    stopword_removal_handler = StopwordRemovalHandler()

    # Set up the chain
    lowercase_handler.set_next(punctuation_removal_handler).set_next(stopword_removal_handler)

    return lowercase_handler
