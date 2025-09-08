#types of inheritance concepts in python
#multipile class
class grandparent:
    def display(self):
        print("big class")
class parent:
    def fdisplay(self):
        print("small class")
class child(parent,grandparent):
    def show(self):
        print("child class")
#multiline class
class car:
    def show1(self):
        print("name:toyato")
class carspeed(car):
    def show2(self):
        print("max")
class car1(carspeed):
    def show3(self):
        print("high")
#hierarchical
class name:
    def get(self):
        print("krishna")
class age(name):
    def h(self):
        print("21")
class id(name):
    def f(self):
        print("174")
c1=child()
c1.display()
c1.fdisplay()
c1.show()
#passing functions of grandparent class and father class from child class
c2=carspeed()
c2.show1()
c2.show2#
c3=car1()
c3.show3()
c2.show2()#accesing derived class functions from another derived class
#passing elements of 2 derived classes from base class .passing with first derived class
c4=age()
c4.get()
c4.h()
