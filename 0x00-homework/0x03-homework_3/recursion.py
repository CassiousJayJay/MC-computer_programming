def main():
   fibonacci()
   fact()
   sum_digits()
   power()

def fact(n):
   if (n == 0):
      return 1
   return n * fact(n-1)
result = fact(5)
print(result)


def sum_digits(n):
    if n == 0:
        return 0
    else:
      return (n % 10) + sum_digits(n // 10)
print (sum_digits(563))

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
print(power(8, 4))


def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
nterms = 8
for i in range(nterms):
    print(fibonacci(i))
