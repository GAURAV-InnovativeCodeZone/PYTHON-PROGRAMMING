
''' Build simple calculator in python'''

print("*************************")
Num1 = eval(input(" Enter the 1st value : "))
Num2 = eval(input(" Enter the 2nd value : "))
opr = input(" Enter the operator : ")
print("*************************")

if opr == "+" :
   print(Num1 + Num2)

if opr == "-" :
   print(Num1 - Num2)
  
if opr == "*" :
   print(Num1 * Num2)
  
if opr == "/" :
   print(Num1 / Num2)
   
if opr != "+" and opr != "-" and opr != "*" and opr != "/" :
   
   print(".....invalid operator please check the operator.....")