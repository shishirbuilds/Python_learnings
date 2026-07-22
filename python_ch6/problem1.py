#to find the greatest number out of 4 numbers entered by user

a1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))
n4 = int(input("Enter number: "))

if(a1>n2 and a1>n3 and a1>n4):
    print("The greatest number is: " ,a1)
elif(n2>a1 and n2>n3 and n2>n4):
    print("The greatest number is: " ,n2)
elif(n3>a1 and n3>n2 and n3>n4):
    print("The greatest number is: " ,n3)
else :
    print("The greatest number is: " ,n4)