def isprime(n):
    if n == 1:
        return "Not prime"
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return "Not prime"
    return "Prime"

count = int(input())

for i in range(count):
    number = int(input())
    print(isprime(number))
