class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f' Name  : {self.name} \n Age   : {self.age :2} \n Grade : {self.grade}'

    def promote(self,swedish,english,math,science,social):
        self.se = swedish
        self.en = english
        self.ma = math
        self.si = science
        self.so = social
        if self.se and self.en and self.ma and self.si and self.so >= 50:
            print (f'{self.name} is promoted to next grade')
        else:
            print (f'{self.name} is not promoted ')


s1=Student(name='Anna', age=15,grade=9)
print(s1.get_info())
s1.promote(70,60,80,50,50)

# print(c.promote(swedish,english,math,science,social))
