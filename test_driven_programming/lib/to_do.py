"""As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO."""

def check_to_do(task):
    if '#TODO' in task:
        return True
    else:
        return False