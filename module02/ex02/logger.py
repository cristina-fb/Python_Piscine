import time
from random import randint
import os

#... your definition of log decorator...
def log(fun):
    f = open("machine.log", "a+")
    t = 0.001
    f.write("(cmaxime)Running: " + '{:20}'.format(fun.__name__) + "[ exec-time = " + str(t) + " ms ]\n")

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
        
    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    #@log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    # for i in range(0, 5):
    #     machine.make_coffee()
    # machine.make_coffee()
    machine.add_water(70)