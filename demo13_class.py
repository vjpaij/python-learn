class Robot_Dog:

    def __init__(self, name_field, breed_field):
        self.name = name_field
        self.breed = breed_field

    def bark(self):
        print("Bow Bow!!!")

# Main Program

my_dog = Robot_Dog("Jimmy","Doberman")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()