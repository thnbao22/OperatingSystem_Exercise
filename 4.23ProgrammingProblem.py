import threading
from math import sqrt
'''Write a multithreaded program that outputs prime numbers. This program
should work as follows: The user will run the program and will
enter a number on the command line. The program will then create a
separate thread that outputs all the prime numbers less than or equal to
the number entered by the user.'''
def Primes(num) -> bool:
    if (num < 2):
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True 

def countPrimes(num):
    for i in range(1, num + 1):
        if (Primes(i)):
            print(i, end = " ")
             

if __name__ == "__main__":
    number = int(input("Please enter a number: "))
    # Create a thread called thread1
    print("All the prime numbers less than or equal to {}: ".format(number), end = " ")
    thread1 = threading.Thread(target = countPrimes, args = (number,))

    # Start a thread
    thread1.start()

    # End the thread exectution
    thread1.join()
