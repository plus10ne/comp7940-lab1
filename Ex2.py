# Write a function that prints all factors of the given parameter x
def print_factor(x):
    for i in range(x+1):
        if i !=0 and x % i == 0:
            print(i)
x = int(input())
print_factor(x)
# your code here