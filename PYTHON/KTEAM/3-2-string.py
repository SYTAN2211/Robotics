#chuoi tran,in moi thu trong chuoi bo qua cac ky tu dac biet:\n,..
print(r"Hello world \nI'm Tan")
print("Hello world \nI'm Tan")

#CAC TOAN TU VOI CHUOI
#1 CONG CHUOI
a= 'Hello World! '
a += 'This is my computer ' #a=a+...

print(a)

#2 NHAN CHUOI
b= "tan "
d=b*5   
print(d)

#3 TOAN TU IN A IN(o trong) B khong? ket qua xuat ra la TRUE or FALSE
str_A = 'Hello World'
str_B = "H"
str_C = str_B in str_A
print(str_C)

#4 CAC TOAN TU SO SANH >,<,==,!=,...

#5 INDEXING VA CAT CHUOI
str_D = str_A[-3]
str_E = str_A[None:len(str_A)]
str_F = str_A[None:None:-2]
print(str_D)
print(str_E)
print(str_F)

#6 EP KIEU DU LIEU
A = '6.5'
B=float(A) + 1.5
print(B,type(B))

#7 THAY DOI NOI DUNG CHUOI
#str_A = 'Hello World'
str_A = str_A[None:4] + 'O' + str_A[5:None]
print(hash(str_A)) #thay doi sau moi lan chay code
print(str_A)