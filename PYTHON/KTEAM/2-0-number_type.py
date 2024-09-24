'''#kieu decimal lay do chinh xac sau dau thap phan nhieu hon
from decimal import*
getcontext().prec = 18

a= Decimal(10)/Decimal(3)
print (a,type(a))

b=10/3
print(b,type(b))

#kieu phan so
from fractions import*
c= Fraction(6,9)
print(c,type(c))

#so phuc
d= complex(1,-2)
print(d,type(d))
print(d.real)
print(d.imag)

#cac phep toan
e,f=10,3
print(e*f)
print(e/f)
print('chia lay nguyen 10//3= ',e//f)

print('chia lay du 10%3= ',e%f)

print('luy thua 10**3= ',e**f)'''

a=3
b=(a:=a+2)+3
print(a,b)

