def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_power_of_five(n):
    return n > 0 and (n & (n - 1)) == 0 and n % 5 == 0
def mnozh_3cifri(a):
    a = abs(a)
    b = a%10
    n = a//10
    c = n%10
    d = n//10
    return b*c*d
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def add(x, y):
    return x + y
def square(x):
    return x ** 2
