#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'                                           #类的帮助信息可以通过ClassName.__doc__查看
    empCount = 0                                              #只在第一次实例化是执行
#empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用Employee.empCount访问。

# 以下为类体，类中定义的函数为类体
    def __init__(self, name, salary):                  #__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.name = name                                    #self 代表类的实例(当前对象的地址)，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        self.salary = salary
        Employee.empCount += 1                      #每实例化一次执行一次
        print(self)

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

#创建实例对象
emp1 = Employee("Zara", 2000)       #使用类的名称 Employee 来实例化，并通过 __init__ 方法接受参数
print(emp1.displayCount())               #使用点(.)来访问对象的属性。
print(emp1.displayEmployee())
emp2 = Employee("Manni", 5000)
print(emp2.displayCount())


emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
print(emp1.age)
#del emp1.age  # 删除 'age' 属性
try:
   print(emp1.age)
except:
   print("No Age")
else:
   print('Age Exist')
finally:
   print('over')

hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)


