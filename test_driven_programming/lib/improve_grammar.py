"""As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter 
and ends with a suitable sentence-ending punctuation mark."""

def check_grammar(input_words):
    if input_words and input_words[0].isupper() and input_words[-1] in '!?.':
        return True
    else:
        return False