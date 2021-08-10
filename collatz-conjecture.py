n = int(input("Enter a number: "))
cur = n

while cur != 1:
    if cur % 2 == 1:
        cur = cur*3+1
    else:
        cur = cur/2

print(str(n) + " follows the Collatz-Conjecture")