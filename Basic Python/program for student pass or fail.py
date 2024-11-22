
 # student pass or fail program

P=int(input("enter physics marks :" ))
C=int(input("enter chemistry marks :"))
M=int(input("enter maths marks :" ))

totalper=(((P+C+M)/300)*100)
print(f"total percentage is {totalper}")

if (P < 33 or C < 33 or M < 33):
	print("you are fail")

elif (totalper > 40):
	print("you are pass")
else:
	print("yor are fail")
	