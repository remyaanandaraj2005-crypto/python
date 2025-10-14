f=open("rymes.txt","r")
content=f.readlines()
l=len(content)
feven=open("evenfile.txt","w")
fodd=open("oddfile.txt","w")
print(l)
print("length of line:",1)
for i in range(l):
    if i%2==0:
        fodd.write(content[i])
    else:
        feven.write(content[i])
f.close()
feven.close()
fodd.close()
    
