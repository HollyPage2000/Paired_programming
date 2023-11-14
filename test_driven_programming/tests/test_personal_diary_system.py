from lib.personal_diary_system import *

def test_make_snippet():
    assert make_snippet('Today i went to the park and saw someone holding an ice cream') == 'Today i went to the ...'
    assert make_snippet('I love pies and mash sir') == 'I love pies and mash ...'    
    

def test_count_words():
    assert count_words('Hello') == 1
    assert count_words('I am Puzzled') == 3
    assert count_words('Today i went to the park') == 6
    assert count_words('i love ice cream so much it hurts') == 8