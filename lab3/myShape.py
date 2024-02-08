class MyShape:
    def __init__(self, color = "brown", is_filled = False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"Shape color: {self.color}, Shape is {filled_status}"
    
    def getArea(self):
        return 0
    
class Rectangle(MyShape):
    def __innit__(self, color = "brown", is_filled = False, x_top_left = 1, y_top_left = 1, lenght = 1, width = 1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.lenght = lenght
        self.width = width

    def getArea(self):
        return self.width * self.lenght
        
    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"Rectangle color: {self.color}, Shape is {filled_status}, Width: {self.width}, Lenght: {self.lenght}"
            


class Circle(MyShape):
    def __innit__(self, color = "Brown", is_filled = False, x_center = 1, y_center = 1, radius = 1):      
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return 3.14159 * self.radius * self.radius

    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"Shape color : {self.color}, Shape is {filled_status}, Radius: {self.radius}" 


color = input()
is_filled = input().lower() == "true"
width = float(input())
lenght = float(input())
rectangle1 = Rectangle(color, is_filled, width, lenght)
print(rectangle1)
