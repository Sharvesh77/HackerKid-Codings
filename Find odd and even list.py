l=[10,34,6,78,89,54,78,46,91,10]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even list: ",even)
print("Odd list: ",odd)