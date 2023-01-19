'''mydict={
    "brand":"Hyundai",
    "model": "i10",
    "year":2001
        }'''
#print(mydict["model"])
#print(mydict["year"])

'''mydict["model"]= "i20"
print(mydict)'''
'''for i in mydict://print only keys
    print(i)'''
'''for i in mydict://print only values
    print(mydict[i])'''
'''for x,y in mydict.items()://print both keys and values 
    print(x,y)'''

'''if "model" in mydict://key is present or not in dict
    print("exist")
else:
    print("not exist")'''

#add itmem in dict

'''mydict["type"]="new"
print(mydict)'''

#delete item in dict
'''mydict.pop("model")
print(mydict)'''
'''del mydict["brand"]
print(mydict)'''

'''mydict.clear()//this will cler all the items in the dict
print(mydict)'''

# copy items from one dict to another

'''mydict2=mydict.copy()
print(mydict2)'''

#thislist = ["apple", "banana", "cherry","watermelon"]
'''for i in thislist:
    print(i)'''
'''for i in range(len(thislist)):
    print(thislist[i])'''
'''while i< len(thislist):
    print(thislist[i])
    i=i+1'''

'''while i < 6 :
    print(i)
    i=i+1'''
'''while i <= 6:
    if i==3:
        i = i + 1
        continue
    print(i)

    i=i+1'''

#12456
'''while i<=6:
    #print(i)
    i=i+1
    if i==3:
        continue
    print(i)'''

#thislist = ["apple","banana","cherry","watermelon"]
'''for i in thislist:
    if i=="cherry":
        break
    print(i)   '''
'''for i in thislist:
    if i=="cherry":
        continue
    print(i)   '''

'''for i in range(6):
    if i<=5:
        print(i)
print("loop end")'''

'''def myfun(first,last):
    print(first,last)
myfun("rajesh","patil")'''
'''def mynum(*test):
    print(test[1])
mynum("veer","sanket","adarsh")'''

'''def my_function(country = "Norway"):
  print("I am from " + country)

#my_function("Sweden")
#my_function("India")
my_function()
#my_function("Brazil")'''
'''def myfunna(test):
    for i in test:
        print(i)



fruits= ["apple","mango","banana"]
myfunna(fruits)'''

''''def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

res1=largest(4,5)
print(res1)'''

'''class myclass:
    def m1(self,a):
        print(a)
result=myclass()
result.m1(10)'''
'''class myclass:
    a,b=20,30
    def m1(self):
        print(self.a+self.b)
res=myclass()
res.m1()'''
'''class myclass:
    def m1(self):
        print("pyhton")
    @staticmethod
    def m2(self,a,b):
        print(self.a,self.b)
res=myclass()'''


'''class test:
    num=34

    def __init__(self):
        print("dsfds")
    def myfun(self):
        print("efewf")


obj=test()
#obj.myfun()
test.num'''

class calculator:
    num=100

    def __init__(self,a,b):
        self.fistnum=a
        self.secondnum=b

    def firstmethod(self):
        return self.fistnum+self.secondnum+calculator.num

firstobj=calculator(2,4)
print(firstobj.firstmethod())



