class OperatorOverload:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;

    def printValue(self):
        print('Vector (',self.a,self.b,')');

    def __add__(self,other):
        return OperatorOverload(self.a+other.a,self.b+other.b);
v1=OperatorOverload(2,10);
v2=OperatorOverload(5,-2);
v3=v1+v2;
v3.printValue();
