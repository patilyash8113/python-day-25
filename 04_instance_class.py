# class employee:
#     company="hp" #this is called attribute
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     # Instance method
#     def get_info(self):
#         info=f"The name is {self.name} and the salary of the employee is {self.salary}"
#         print(info)
#     @staticmethod #static method is mehod that dont require any first argument like "self".
#     def sum(a,b):
#         return a+b
    
#     @classmethod #class method convert a function to class method
#     def print_company(cls):
#         print(cls.company)

#     @classmethod
#     def change_company(cls,new_comany):
#         cls.company=new_comany
       




# e1=employee("yash",35000)
# e2=employee("bablu",50000)
# # print(employee.company)
# # print(employee.name) #this will show error because we dont have any name variable for employee class
# # e1.get_info()
# # e2.get_info()

# # print(e2.sum(5,5))

# e1.print_company()
# # e1.change_company("ACER")
# # e1.print_company()
# print(employee.company)
# e1.change_company("ACER")
# e1.print_company()


class employee:
    company="Tesla"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get_info(self):
        info=f"The name of the Employee is {self.name} and the salary of the Employee is {self.salary}"
        print(info)
    
    @staticmethod #static method dont need to 1st argument..
    def mul(a,b):
        return a*b
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod
    def change_comapny(cls,new_company):
        cls.company=new_company

e1=employee("Yash",20000)
e2=employee("mahesh",30000)
print(employee.company)
e1.get_info()
e2.get_info()
print(e1.mul(5,5))
print(e2.mul(10,10))
print(employee.company)
e1.change_comapny("SPACEX")
e1.print_company()

class student:
    school="jpschool"

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def get_info(self):
        info=f"The name of the student is {self.name} and the Roll no of the student is {self.rollno}"
        print(info)
    def print_school(cls):
        print(cls.school)
    def change_school(cls,new_school):
        cls.school=new_school

        

e1=student("YASh",21)
e2=student("ANUJ",20)
print(student.school)
e1.get_info()
e2.get_info()
print(student.school)
e1.change_school("APschool")
e1.print_school()

    