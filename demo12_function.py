def greeting_local(name):
    print("Hello", name)

def greeting_global():
    print("Hello", name_global)


# Main Program
name_local = input("Enter your name:\n")
greeting_local(name_local)

name_global = input("Enter your name:\n")
greeting_global()
