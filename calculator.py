print("1.add")
print("2.mul")
choice=int(raw_input("Enter your choice "))
num1=int(input("num1 is:"))
num2=int(input("num2 is:"))
if(choice==1):
  print(num1+num2)
elif(choice==2):
  print(num1*num2)
else:
  print(num1-num2)
