import prime_func

while 1:
    n = int(input("Input number(0 : Quit) : "))
    check = False
    if n == 0:
        break
    elif n == 1:
        print("re-enter number~!!")
    else:
        check = prime_func.is_prime_number(n)
        if check:
            print(f"{n} is a prime number")
        else:
            print(f"{n} is not a prime number")