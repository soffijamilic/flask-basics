def factorize(n):
    factors = []
    i = 2
    while n >= i:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

def number_of_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count