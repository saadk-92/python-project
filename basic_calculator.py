import operator
print ("This Simple calculator based on two input fuction")
a = float (input ("Enter a value 1 : "))
b = float (input ("Enter a value 2 : "))
i = input ("Please select the operator [+,-,*,/] : ")

if i == "+" :
    x = operator.add(a,b);
    print ("The value is : ",x)
elif i == "-" :
    x = operator.sub(a,b);
    print ("The value is : ",x)
elif i == "*" :
    x = operator.mul(a,b);
    print ("The value is : ",x)
elif i == "/" :
    if b !=0 :
         x = operator.truediv(a,b);
         print ("The value is : ",x)
    else:
         print ("Input number 2 error")
else:
    pass