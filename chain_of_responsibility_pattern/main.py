# main.py
from setup_chain import setup_chain

# Set up the chain
cleaning_chain = setup_chain()

# Sample text
text = "Hello World! This is a test sentence to demonstrate the Chain of Responsibility pattern."

# Clean the text
cleaned_text = cleaning_chain.handle(text)
print(cleaned_text)
