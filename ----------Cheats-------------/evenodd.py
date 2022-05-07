num = input("Enter numbers : ").split() 
even=odd=0

for i in num:
if int(i)%2 == 0: 
even+=1
else:
odd+=1

print('Number of even numbers is ',even) 
print('Number of odd numbers is ',odd)
