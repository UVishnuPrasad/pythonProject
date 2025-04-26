x = int(input("Enter a number to calculate factorial"))
fact = 1
for i in range (1,x+1):
    fact += fact * (i-1)
print(fact)