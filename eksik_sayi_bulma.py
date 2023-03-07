import random
list1=[]
degisken = int(input("bir tek sayı giriniz: "))
sira=0
eksiksayi=int(0)
rnd = random.randint(0,degisken)
rndSy = int(1)
if rnd %2 == 0:
    rndSy = int(rnd+1)
    if rndSy >degisken:
        if degisken %2 ==1:
            rndSy=int(degisken)
        else:
            rndSy=int(degisken-1)
print(rndSy)
for i in range(1, degisken+1):
    if i%2 !=0:
        if i!=rndSy:
            list1.append(i)
print(list1)
print( (f"{rndSy} eksik sayı"))





