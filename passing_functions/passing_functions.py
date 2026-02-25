def decorator(func):
    def wrapper():
        print("code before the func executes")
        func()
        print("code after the func executes")

    return wrapper


def heloo():
    print("hello")


function = decorator(heloo)

function()
