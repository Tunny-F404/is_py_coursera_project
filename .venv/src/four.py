a = [1,2,3,4,5,6,7,8,9,0]
b = [108, 105, 115, 116]

class a_car:
    def __init__(self,b,a):
        self.b = b
        self.a = a
    def pa(self):
        print(self.a)
    def pb(self):
        print(self.b)
    def __del__(self):
        print('***********')

car = a_car(b,a)
car.pb()
car.pa()

car = 43