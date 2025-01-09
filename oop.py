class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width

n=rectangle(20,30)
print(f"Area of rectangle is {n.area()}")