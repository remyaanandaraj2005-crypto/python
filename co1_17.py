dic = {}
limit = int(input("Enter the limit: "))  

for i in range(limit):  
    k = input("Enter the key: ")  
    val = input("Enter the value: ")  
    dic[k] = val 
print("In ascendind order")
print(dict(sorted(dic.items())))
print("In Desending order")
print(dict(sorted(dic.items(),reverse=True)))

