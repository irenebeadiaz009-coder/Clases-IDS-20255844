"""manzana = int(input())

if manzana % 2 == 0:
    print(manzana/2)
else:
    print((manzana*3)+1)"""
    
lenn=int(input()) 
idn=int(input()) 
lcj=int(input())
isnd=int(input()) 
tupla= (lenn, idn, lcj, isnd) 
nombres= ("LEN", "IDN", "LCJ", "ISND") 
print(nombres[tupla.index(max(tupla))]) 