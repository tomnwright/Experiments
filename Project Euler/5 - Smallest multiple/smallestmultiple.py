# https://projecteuler.net/problem=5

def multiple_of_all(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


def max_val():
    product = 1
    for i in range(1, 21):
        product *= i
    return product


t = 20
while t <= max_val():
    if multiple_of_all(t):
        print(f"Found: {t}")
        break

    t += 20
    if t % 5000000 == 0:
        print(t)


