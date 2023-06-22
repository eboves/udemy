n = int(input("Check this number: "))

def prime_checker(number):
    if number % 2 != 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(number=n)