class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print("Name is :\n", self.name)

    def walk(self, x, y):
        self.position[0] = self.position[0] + x
        self.position[1] = self.position[1] + y
        print("New position : \n", self.position)

    def eat(self):
        print("I need food")


class Robot_Dog(Robot):
    def make_sound(self):
        print("Woof Woof!!!")

    def eat(self):
        super().eat()
        print("I need chicken")

# Main Program
my_robot_dog = Robot_Dog('Jimmy')
my_robot_dog.walk(10,20)
my_robot_dog.make_sound()
my_robot_dog.eat()
