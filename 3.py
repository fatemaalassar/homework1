import json
file=open('j.json','r')
j=json.load(file)
file.close()
i=0
for a,b in j.items():
    an=input(a)
    if an==b:
        i+=1
name=input('enter your name: ')
l=['your name is ',name,' your resault is',i]
outfile='o.json'
outfile=open(outfile,'w')
json.dump(l,outfile)
outfile.close()
print(l)
