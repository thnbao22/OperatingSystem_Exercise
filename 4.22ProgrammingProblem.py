import threading

# initialize global variables
averageNum = 0
def calculateAverage(numbers) -> None:
    global averageNum
    averageNum = sum(numbers) / len(numbers)
    print("The average number is {}".format(int(averageNum)))

def findMax(numbers) -> None:
    print("The maximum value is {}".format(max(numbers)))

def findMin(numbers) -> None:
    print("The minimum value is {}".format(min(numbers)))
if __name__ == "__main__":
    arr = [90, 81, 78, 95, 79, 72, 85]
    
    # Create three threads
    
    thread1 = threading.Thread(target = calculateAverage, args = (arr,))
    thread2 = threading.Thread(target = findMin, args = (arr,))
    thread3 = threading.Thread(target = findMax, args = (arr,))

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()

    # End 
    thread1.join()
    thread2.join()
    thread3.join()