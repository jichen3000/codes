def __linux_get_name():
    return "linux"

def __win_get_name():
    return "win"

# it is a good alternative to avoid using eval to get a function
print globals()['__linux_get_name']()