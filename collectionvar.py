#replace element based on index
#list1=["mango","banana","apple"]
'''list[1]="watermelon"
print(list)'''
# if in list
'''if "banana" in list:
    print("banana is present")
else:
    print("banana is npt present")'''

# append and insert method

#list.append("watermeln")
#print(list)

#insert
'''list.insert(1,"watermelon")
print(list)'''
# remove items in list
#pop
'''list.pop(1)
print(list)'''

#del
'''del list[2]
print(list)'''
#clear
'''list.clear()
print(list)'''
#copy list
'''list2=list(list1)
print(list1)
print(list2)'''
'''list2=list1.copy()
print(list2)'''

#adding two list
#using loop
#list2=[1,2,3]
'''for i in list2:
    list1.append(i)
print(list1)'''
#using + operator
'''list3=list1+list2
print(list3)'''
'''list1.extend(list2)
print(list1)'''

mytuple=("mango","banana","apple")
mylist=list(mytuple)
mylist[1]="watermelon"
mytuple=tuple(mylist)
print(mytuple)








