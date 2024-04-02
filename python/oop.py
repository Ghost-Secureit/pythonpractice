#Classes 



class superAdmin(object):
    isAdmin = True
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        print('New user created!')
        
    def speak(self):
        print('Hi, im ', self.name, 'and im ', self.age, 'years old!')
        print('I am super Admin')

    def changeAge(self, age):
        self.age = age


class newUser(superAdmin):
    isAdmin = False
    def __init__(self, name, age):
        super().__init__(name, age)
        self.age = 24

    def speak(self):
        print('Hi, im ', self.name, 'and im ', self.age, 'years old!')
        print('Im not super Admin')


class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price 
        self.gas = gas 
        self.color = color

    def fillTank(self): 
        self.gas = 100
    
    def emptyTank(self):
        self.gas = 0 

    def gasLeft(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color,speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def Horn(self):
        print('honka honka')         


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 
        self.coords = (self.x, self.y)
    
    def move(self, x, y):
        self.x += x
        self.y += y 
    
    def __add__ (self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mult__(self, p):
        return self.x * p.x + self.y * p.y
    
    
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) +')'


p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)
p5 = p1 + p2
p6 = p4 - p1
#p7 = p2 * p3

print(p5, p6)
        




ghost = superAdmin('Ghost', 29)
jay = newUser('Jay', 27)
ghost.speak()
jay.speak()

corvette1 = Car(1000, 100,'red', 'fast')
corvette1.Horn()