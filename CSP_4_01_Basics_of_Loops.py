#import random

def oddNumbers(n: int) -> str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string separated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            result.append(str(i))
    return " ".join(result)


def backwards(n) -> str:
    """
    modify the below function such that it prints out all the numbers from n to 1 inclusive
    starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    result = []
    for i in range(n, 0, -1):
        result.append(str(i))
    return " ".join(result)


def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10.
    Then print out how many times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    tries = 0
    while True:
        num = random.randint(1, 10)
        tries += 1
        print(num)
        if num == 10:
            break
    print(f"it took {tries} tries to get a 10")


def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times.
    Then after that is done print out what the highest number and the lowest number was
    from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
    highest = -1
    lowest = 101
    for i in range(n):
        num = random.randint(1, 100)
        print(num)
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


def reverse(word: str) -> str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    result = ""
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    return result


def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers from 1 to n(inclusive).
    Fizz buzz is defined as if the number is divisible by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.
    As with above questions add each answer to a string and return the final string.
    :param n:
    :return:
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return " ".join(result)


def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2.
    if n is an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    result = []
    while n >= 1:
        result.append(str(n))
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    return " ".join(result)


def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci sequence
    in a single string separated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as the first two numbers.
    Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    if n <= 0:
        return ""
    if n == 1:
        return "0"

    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(str(a))
        a, b = b, a + b
    return " ".join(result)


# Test the functions
print(fibonacci(300))