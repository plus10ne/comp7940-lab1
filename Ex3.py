# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

for i in range(4):
    for j in range(l[i]+1):
        if j != 0 and l[i] % j == 0:
            print(j)
# your code here