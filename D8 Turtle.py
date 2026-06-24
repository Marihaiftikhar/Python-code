import turtle as t
class shape:
    def __init__(self,size,color):
        self.size = size
        self.color = color
        
        self.pen = t.Turtle()
        self.pen.color(color)
    def draw_square(self):
        for i in range(4):
            self.pen.forward(self.size)
            self.pen.right(90)
    def draw_circle(self):
        self.pen.circle(self.size)
    def draw_triangle(self):
        for i in range(3):
            self.pen.forward(self.size)
            self.pen.left(120)
    def draw_star(self):
        for i in range(5):
            self.pen.forward(self.size)
            self.pen.right(144)
while True: 
    print("1.sqaure")
    print("2.circle")
    print("3.triangle")
    print("4.star")
    print ("5.exit")
    choice = input("enter your choice:")
    if choice == "5":
        print("exit")
        break
     
    size =  int(input("enter the size:"))
    color = input("enter the color you want:")
    s = shape( size , color) 
    if choice == "1":
        s.draw_square()
    elif choice == "2":
        s.draw_circle()
    elif choice == "3":
        s.draw_triangle()
    elif choice == "4":
        s.draw_star()
    else:
        print("invalid choice")
t.done()
        
