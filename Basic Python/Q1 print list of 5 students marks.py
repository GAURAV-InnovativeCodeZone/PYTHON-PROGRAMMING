
# write a program to accept marks of 5 students and display them in sort manner.

E = input("enter  1st student marks : " )
M = input("enter 2nd student marks : ")
S = input("enter 3rd student marks : ")
P = input("enter 4th student marks: " )
C= input("enter 5th student marks:  ")

marks_list = [E, M, S, P, C]
print(marks_list)

marks_list.sort()
print(marks_list)