# keyword and positional arguments
'''def detali (id,name,mailid):
    id=24
    name="bunny"
    mailid="bunny@gmaili.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid",)'''






'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name", mailid="mailid")
details(id=20,name="bunny",mailid="bunny@gmaili.com")
details(id="30",name="sai",mailid="bunny@gmaili.com")
details(40,"virat","virat@gmaili.com")
detailis("virat","virat@gmaili.com",50)
details(name="vijay",mailid="v@gmaili.com",id=60)'''




#default arguments
'''def Grocery(item,price):
 print("item is %s" %item)
 print("price is %.2f" %price)
Grocery("rice",1500)''' 


'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''


#cake,price,quantity
'''def bakery(cake,price,quantity):
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %s"%quantity)
bakery("cake", 250,"1kg")'''   




#* arguments(* is used to unpack the element)

'''a=(10,20,30,40,50)
print(a)
print(*a)'''

'''a=(10,20,30,40,50)
print(a)
prnt(*a)'''

'''a={10,20,30,40,50}
print(a)
print(*a)'''

'''a={"year":2026,"month":"july"}
print(a)
print(*a)'''

'''a,*b,c=2,3,4,5,6,7,8,9,0
print(a)
print(*b)
print(c)'''


'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''
