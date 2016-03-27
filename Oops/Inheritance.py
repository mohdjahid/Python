class Parent(object):      # define parent class
    parentAttr=100;
    def __init__(self):
        print('Calling Parent Constructor');

    def parentMethod(self):
        print('Calling Parent Method');

    def setAttr(self,attr):
        Parent.parentAttr=attr;

    def getAttr(self):
        print('Parent Attrbute : ',Parent.parentAttr);

class Child(Parent): # define child class
    def __init___(self):
        parent('Calling child Constructor');

    def childMethod(self):
        print('Calling Child Method');
        
c=Child();
c.childMethod();
c.parentMethod();
c.setAttr(200);
c.getAttr();
