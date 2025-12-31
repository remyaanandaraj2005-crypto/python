#csv writing
import csv
f=open("rwrirea.csv","w",newline='')
l=int(input("Enter the number of students:"))
content=csv.writer(f)
content.writerow(["Name","Grade","RollNo"])
for i in range(l):
           Name=input("Enter Your Name:")
           Grade=input("Enter Your Grade:")
           RollNo=int(input("Enter Your Roll no:"))
           lis=[Name,Grade,RollNo]
           content.writerow(lis)
f.close()

#csv reading
f1=open("rwrirea.csv","r")
content=csv.reader(f1)
next(content)
for i in content:
           print(i)
f.close()
