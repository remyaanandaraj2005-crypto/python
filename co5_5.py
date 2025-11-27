#input dictionary using user input
import csv
data={}
n=int(input("enter the limit:"))
for i in range(n):
    key=input("enter the key:")
    value=input("enter the value:")
    data[key]=value
print(data)
#csv writing
f=open("dictdata.csv","w",newline="")
content=csv.writer(f)
content.writerow(data.keys())
content.writerow(data.values())
f.close()
#csv reading
f1=open("dictdata.csv","r")
content=csv.reader(f1)
for i in content:
        print(i)
f.close()
