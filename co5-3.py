import csv

file = open("demo2.csv", "r")
content = csv.reader(file)
f = int(input("Enter the number: "))

for i in content:
    print(i)


