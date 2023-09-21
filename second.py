class employees:
    department = 'engineering'

    def __init__(self,name,role,salary):
        self.name= name
        self.role=role
        self.salary=salary
    def showdescription(self):
        print(self.name, 'is a',self.role,'with an annual salary of', self.salary,'and works in the',
              self.department,'department')
    def changename(self,name):
        self.name= name
        print('the employees name has been changed to ',self.name)
    def changerole(self,role):
        self.role= role
        print('the employees role has been changed to', self.role)
    def changesalary(self,salary):
        self.salary = salary 
        print('the employees salary has been changed to', self.salary)

    

h = employees('Hubert Akanson','data analyst','USD80,00.00')

h.changesalary('USD120,000.00')
h.changerole('Technical Project Manager')
h.showdescription()