m1 = int(input("Enter marks: "))
m2 = int(input("Enter marks: "))
m3 = int(input("Enter marks: "))

tot_per = ((100)*(m1+m2+m3))/300

if(tot_per>=40 and m1>=33 and m2>=33 and m3>=33):
    print(tot_per)
    print("Pass")

else :
    print("Fail")