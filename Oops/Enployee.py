class Employee:
    'Common base class for employees'
    empCount=0;

    def __init__(self,name,salary):
        self.name=name;
        self.salary=salary;
        Employee.empCount+=1;

    def displayCount(self):
        print('Total Employyes ',self.empCount);

    def displayEmployee(self):
        print('Name : ',self.name,' Salary : ',self.salary);

emp1=Employee('Jahid',2000);
emp2=Employee('Rahil',2000);
emp1.displayEmployee();
emp1.displayCount();
emp2.displayEmployee();
emp2.displayCount();
print('Total Employees ',Employee.empCount);
