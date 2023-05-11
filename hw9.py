class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def set(self,x,y):
        self.x=x
        self.y=y

    def get(self):
        return (self.x, self.y)
    
class Rectangle:
    lt=Point()
    rb=Point()
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        Rectangle.lt.set(self.x1,self.y1)
        Rectangle.rb.set(self.x2,self.y2)

    def show(self):
        print(f'좌측 상단 꼭지점이 {Rectangle.lt.get()}이고 우측 상단 꼭지점이 {Rectangle.rb.get()}인 사각형입니다.',end='')

    def getWidth(self):
        return self.x2-self.x1

    def getHeight(self):
        return self.y1-self.y2

    def getArea(self):
        return self.getWidth()*self.getHeight()

    def getPerimeter(self):
        return (self.getWidth()+self.getHeight())*2
    
r1 = Rectangle(5, 10, 20, 5)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
