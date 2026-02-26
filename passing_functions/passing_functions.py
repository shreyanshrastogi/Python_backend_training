
def decorator(func):
    #wrapper around the function
    def wrapper():
        print("code before the func executes")
        func()
        print("code after the func executes")
    #returning wrapped function
    return wrapper

# independent function
def heloo():
    print("hello")

# decorating the function
function = decorator(heloo)
# calling new function which refers to wrapper inside decoraotor which contains our function heloo with some other code before and after it
function()
