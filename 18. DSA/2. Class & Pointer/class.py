# Class - is like a cookie cutter. we can make our own data structure. it has it own syntax.


class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie("green")
cookie_two = Cookie("red")

print(f"Cookie one is {cookie_one.get_color()}")
print(f"Cookie two is {cookie_two.get_color()}")

cookie_one.set_color("yellow")

print(f"Cookie one is {cookie_one.get_color()} now")
print(f"Cookie two is still {cookie_two.get_color()}")