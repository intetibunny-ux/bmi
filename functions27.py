# funcations
#1 a function is block organized reusable and that is us perform a single or multiple task.
#2 python is inbilt function like print,u can make your own funtion and thes are user defind function.
#3 function block being with keyword def follewed by the function name and perameters( () )

'''a=10
b=20
print("the sum is ",a+b)
print("the diff is",a-b)
print("the prouduct is",a*b)'''

'''a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the prouduct is",a*b)'''

#**,%//
'''def calculate(a,b):
    print("the pow is",a**b)
    print("the intdiv is",a//b)
    print("the modeius is",a%b)'''


while true:
'''  def add():
      a=int(input("a value"))
      b=int(input("b value"))
      print(a+b)
      add()
   add()'''

#difference betwen return
#print: just show the human user output in a concel
#return:return is akey word and retun is used to terminate and gives back a value from the function
#print v/s return
'''def mul(a,b):
    print(a*b)
mul(4,5)'''

'''def mul(a,b):
    return a*b
print(mul(4,6))'''


'''def cal(a,b):
    c=a+b
    b=a-b
    e=a*b
    print(c)
    print(b)
    print(e)
cal(2,3)'''


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(4,6))'''
    
a=4
b=6
'''def cal(a,b):
    print("sum of a+b")
    print("diff ofa a-b")
    print"product of a*b")
print(cal(4,6)'''



while True:
   def cal():
       a=int(input("a value"))
       b=int(input("b value"))
       option=int(input('''choose the option 1.add/ 2.sub/ 3.mul'''))

       if option==1:
           add()
       elif option==2:
           sub()
       elif option==3:
           mul()
       
