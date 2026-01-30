# python-day-25
Day 20 of my python journey
Today I revised previous concepts and learn static method, class method and instance method.
1)static method= static method is method that dont require any first argument like "self" . This methods are essential regular function that are logically grouped within a class for organizational purpose

2)class method = class method is method that any function into class method
A class method is marked using @classmethod decorator. class method are often used for modifying class atrributes and factory methods..
Eg. suppose we create class Animals and that animal class have variable called species and that species variable have value mammals after that suppose i want to change the species from mammals to reptile so we create function called set_species , the set_sepcies have argument called new species . so bacically here i change class species using function using @classmethod . after that i create get_species function using class methods. so whenever i try to print it first i need to print animal.get_species and after that we set a species and then we again print animal.get_species and now we have new printed values called reptile because i set new_species = "reptile".

3)instance method(default)
These are the most common type of method. they operate on instance of the class (object) and have access to the instance data through the self parameter.
