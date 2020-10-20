a=10
b=20
c=a+b
print(c)

def f1():
    pass
def f2():
   a=333
   X=10
   print(111)
   

lst=[]
f1_ret=f1()
f2_ret=f2()
print(lst.append(f2_ret))
print(lst.append(f1_ret))
print(lst)