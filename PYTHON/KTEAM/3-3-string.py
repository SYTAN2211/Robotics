print("\n")
#Dinh dang bang toan tu %
a = 'toi co %d qua %s' %(5,"trung")
print("a = ", a )

b = 'toi co %.3f qua %s' %(5.333333,"trung")
print("b = ", b)

#Dinh dang bang chuoi f-spring
c = f"c =  {a}" 
print(c)

#Dinh dang bang phuong thuc format
d = 'ten:{2},tuoi{3}'.format(1,2,3,4,5)
print("d = ",d)
#dung format de can le
e = '{:-^50}'.format('Ho Sy Tan') #can le trai:<, can le phai:>
print('e = ',e)
f = '{:->50}'.format('Viet Nam') #can le trai:<, can le phai:>
print('f = ',f)
g = '{:-<50}'.format('Viet Nam') #can le trai:<, can le phai:>
print('g = ',g)

print("\n")