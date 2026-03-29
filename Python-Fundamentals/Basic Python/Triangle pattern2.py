""" OBJECTIVE : To create inverted right-angled triangle pattern """

# n, the number of rows
# i, current row index in outer loop
# j, current row position or column in inner loop

n = 10
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
