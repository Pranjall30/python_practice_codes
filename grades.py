# Give grade based on marks

m = int(input("Enter the marks: "))

if(100>=m>=80):
    print("Grade A")
elif(80>m>=60):
    print("Grade B")
elif(60>m>=40):
    print("Grade C")
else:
    print("Fail")