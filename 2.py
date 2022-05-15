s=input('enter a decimal num ')
d=int(s)
l=[]
while d>0:
    a=str(d%2)
    l.append(a)
    d//=2
l.reverse()
print(" ".join(l))

