def is_prime_number(num):
    isPrime = True

    for i in range(2, num):1
        if num % i == 0:
            isPrime = False

    return isPrime

def main():
    inNum = int(input())
    if is_prime_number(inNum):
        print("is")
    else:
        print("not")

    inNum = int(input())
    primeList = []
    for num in range(2,inNum):
        if is_prime_number(num):
            primeList.append(num)

    print(primeList)

main()


