import pickle,employee


while(1):
ch=int(input("1.Write in File\n2.Read from File\n3.Append in File\n4.Create Pickle\n5.Load Pickle\n6.Exit\n"))
if ch==1:
fo = open("test.txt","w")
s1 = input("Write content : ") fo.write(s1)
fo.close() elif ch==2:
fo = open("test.txt","r") s1 = fo.read()
print(s1) fo.close()
elif ch==3:
fo = open("test.txt","a")
s1 = input("Write content : ") fo.write(s1)
fo.close() elif ch==4:
f=open("employeepickle.dat","wb")
 
n=int(input("Enter number of Employees :")) for i in range(n):
id1 = int(input("Enter ID of Employee%d	:"%(i+1))) name = input("Enter Name of Employee%d :"%(i+1)) sal = input("Enter Salary of Employee%d:"%(i+1)) s=employee.employee(id1,name,sal)
pickle.dump(s,f) f.close()
elif ch==5: f=open('employeepickle.dat','rb') for i in range(n):
s1=pickle.load(f)
if int(s1.sal)>=5000:
print("ID of Employee%d	:"%(i+1),s1.id1) print("Name of Employee%d :"%(i+1),s1.name) print("Salary of Employee%d:"%(i+1),s1.sal)
f.close() elif ch==6:
exit()
