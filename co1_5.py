l=int(input("Enter the limit:"))
list=[]
for i in range(l):
      no=int(input("Enter the numbers:"))
      if(no>100):
            list.append('over')
      else:
           list.append(no)
print(list)
     
