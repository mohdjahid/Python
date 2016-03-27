class Parent:  #define parent class
    def myMethod(self):
        print('Calling Parent class Method');

class Child(Parent):
    def myMethod(self):
        print('Calling Child class Method');
c=Child();
c.myMethod();
