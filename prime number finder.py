L = 0
M = 0
E = 0
F = 0

def is_prime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
           #print(i, end=" ")
           return False

    return True


while (L < 3 and M < 3 and E <= 3 and F == 0):

    users_input = input("Enter your name: ")
    if users_input in users_input == "ME":
        print("your username is:", users_input)
        E = E + 1
        passwords_input = input("Enter your password: ")
        if passwords_input in passwords_input == "wtvr":
            print("your password is:", passwords_input)
            F = F + 1

            while True:
                print("Enter any number 'N' such that N>2 to find the prime numbers within the range between 2 and N; or type 'end' to exit the program")
                prime_numbers_input = input("Your desired number is: ")
                #print("your prime numbers are: ")
                if prime_numbers_input in prime_numbers_input == "end":
                    print("You have Ended the Program.", "Thank You!")
                    break
                print("your prime numbers are: ")
                N=int(prime_numbers_input)
                if N <= 2:
                    print("enter a value greater than 2")
                for i in range(2, N + 1):
                    if is_prime(i):
                       print(i , end=" ")
                print("\ndone")
        else:
            print("error")
            M = M + 1
    else:
        print("error")
        L = L + 1
    if M >= 3 or L >= 3:
        print("you have been locked out")








