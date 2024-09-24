#python tu hieu kieu du lieu ma khong can khai bao truoc
#kieu so nguyen (int) co gia tri luu duoc khong gioi han
a=123
print (type(a))

#kieu so thuc (float) gioi han do chinh sac sau thap phan la 15 chu so
b=1.2222222222222222233444
print (type(b))
print (b)

#de tang do chinh xac dung kieu decimal
#khai bao goi thu vien
#lay moi thu(*) tu thu vien Decimal
from decimal import*

#do chinh xac la bao nhieu chu so ca phan thap phan(co the de mac dinh khong dung)
getcontext().prec = 20

c = Decimal(10)/Decimal(3)
print (type(c))
print (c)

#so sanh neu khong dung Decimal
d=10/3
#d thuoc kieu float
print (type(d))
print (d)
