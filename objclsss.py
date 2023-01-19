'''a,b=12,24
class myfav:
    a,b=30,45

    def fun1(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])
test=myfav()
test.fun1(20,20)'''

'''class mycls:
    staticmethod
    def m1(self,a):
        print(self,a)
mycls.m1(22,24)'''

#constructor example

'''class myclasss:
     def __init__(self,number,name,salary):
         self.number=number
         self.name=name
         self.salary=salary

     def display(self):
         print(self.number,self.name,self.salary)
test=myclasss(2,"baner",22000)
test.display()'''

'''class mycls:
    def __init__(self,name,number,unum):
        self.name=name
        self.number=number
        self.unum=unum
    def __str__(self):
        return(self.name)

test=mycls("hhi",12,1)
print(test)'''

class ab:
    def m1(self):
        print("m1")
    def m2(self):
        print("m2")

test1=ab()
test1.m1()


