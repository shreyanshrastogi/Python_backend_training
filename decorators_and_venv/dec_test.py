def uppercase_decortor(func):
    def wrapper():
        returned_value = func().upper()
        return returned_value

    return wrapper


@uppercase_decortor
def heloo():
    print("brother")
    return "hello"


@uppercase_decortor
def greet():
    print("sir")
    return "greet"


print(heloo())
print(greet())
