
def fun(n):
    n = 1000000000
def fun1(tupla):
    print(tupla)
    tupla += (4,)
    print(tupla)
    return tupla

renglon = ("producto 1",3,100)

renglones = (renglon,renglon,renglon)

print(renglones)

total = 0
for renglon in renglones:
    importe = renglon[1]*renglon[2]
    total += importe
    print(renglon,importe)
print("total: ",total)

t = (1,2,3)
t = fun1(t)
print(t)
x = 4
fun(x)
print('x:',x)






