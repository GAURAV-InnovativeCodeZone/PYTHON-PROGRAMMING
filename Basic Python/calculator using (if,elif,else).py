''' Build simple calculator in python'''

print("*************************")
Num1 = eval(input(" Enter the 1st value : "))
Num2 = eval(input(" Enter the 2nd value : "))
Operator = input(" Enter the operator : ")
print("*************************")

if Operator == "+" :
   print(Num1 + Num2)

elif Operator == "-" :
   print(Num1 - Num2)
  
elif Operator == "*" :
   print(Num1 * Num2)
  
elif Operator == "/" :
   print(Num1 / Num2)
   
else :
   print(".....invalid operator please check the operator.....")
