The problem - A user wants to be aware of their #TODO tasks, and also check if a piece of text contains #TODO.

def check_to_do(task):
    if '#TODO' in task:
        return True
    else:
        return False
        
#A function designed to recieve strings known as tasks

#Returns True if the string passed through the function include '#TODO'
#returns False if the string passed through the function does not include '#TODO'

Example tests:

#initially test if a task containing 'TODO' returns True

def test_does_string_have_TODO():
    assert check_to_do('#TODO: need to clean the house') == True

#Test if a string not containing 'TODO' returns False

def test_string_does_not_TODO():
    assert check_to_do('i need to clean the house') == False
    
#Test if an empty string returns False

def test_empty_string():
    assert check_to_do(' ') == False
