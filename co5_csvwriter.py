import csv
f=open("m4.csv","w")
content=csv.writer(f)
for i in range(1):
    name=input("enter the name")
    age=input("enter the age")
    mark=input("enter the mark")
    l=[name,age,mark]
    content.writerow(l)
f.close()
f1=open("m4.csv","r")
content=csv.reader(f1)
for i in content:
    print(i)
