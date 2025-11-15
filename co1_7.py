#enter two list of integers check whether two list sum same value whether any value occur in both
n1=int(input("Enter the limit of first list:"))
list1=[]
for i in range(n1):
           num=int(input("Enter the numbers of first list:"))
           list1.append(num)
n2=int(input("Enter the limit of second list:"))
list2=[]
for i in range(n2):
           num=int(input("Enter the numbers of second list:"))
           list2.append(num)
if len(list1)==len(list2):
           print("Both list have same length.")
else:
           print("lists have different length.")
if sum(list1)==sum(list2):
           print("Both lists have same sum.")
else:
           print("lists have different sum.")
c=0
status=False
for j in list1:
  if j in list2:
           status=True
           c=c+1
if status==True:

           print("List have coman value.",c)
else:
           print("List have different value.")
