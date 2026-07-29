#veribale length argument's : veribale length arguments are automatically store in tupie and  we use *argument
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,)
b=[4,5,6,7,8888]
check(*b)
c={6,7,8,9,10}
check(*c)
d={"name":"bunny","city":"mtm"}
check(*d)'''


'''def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6,7)
check1(1,3,4,5.3,6.3)
check1(3,4,5,6.4,7.3,8,"bunny",5+9j,True)'''



#kwargs(**)
'''def check(**a):
  print(a)
  print(type(a))
check()
details{"idnos":[10,20,30],
        "name":["bunny","sai","virat"]
        "status":["a","p","a"]}
            check(**details)'''





#both * and ** usage

'''def final(*a,**b):
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
date=(2,3,4,3.5,6.2)
details={"idnos":[10,20,30],
         "name":["bunny","sai","virat"],
         "status":["a","p","a"]}
final(**details)
final(*date,**details)'''


#max(),min(),sum()
'''print(max(5,7,9,20,40))
print(min(4,7,8,9,11,12))'''








#mark analysis report
a= int(input("enter no.of students:"))
marks=[]

for i in range(1,students+1):
    mark=input(f"enter student{i} marks")
    marks.append(mark)

 for i in marks:500
 prints(i)
print(".........marks analysis report.......")
print("total students",students)
print("heighest marks",max(marks))
print("lowest marks", min(marks))
print("total marks",sum(marks))
print("avg", sum(marks)/students)
    
