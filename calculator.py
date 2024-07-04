x=float(input("Enter the first number:"))
y=float(input("Enter the second number:"))
print("what do you want")
what_do_you_want=["sum","subtraction","division","multiple","remainder"]
print(what_do_you_want)
c=input()
if "sum"in c: 
    print("the sum is ",x+y)
if "subtraction"in c: 
 print("the subtraction is ",x-y)
if "division"in c: 
 print("the division is ",x/y)
if "multiple"in c: 
 print("the multiple is ",x*y)
if "remainder"in c: 
 print("the remainder is ",x%y)