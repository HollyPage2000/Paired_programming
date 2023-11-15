from lib.to_do import *

def test_does_string_have_todo():
    assert check_to_do('#TODO') == True
    assert check_to_do('#TODO - Clean bedroom') == True
    
def test_string_does_not_have_todo():
    assert check_to_do('') == False
    assert check_to_do('sort laundry') == False

