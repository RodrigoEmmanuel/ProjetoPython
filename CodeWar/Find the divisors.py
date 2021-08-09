# Find the divisors!
#
# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
# c
# Example:
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"
#

def divisors(integer):
    number = integer-1
    allDivisors = []
    allDivisorsReversed = []
    while number > 1:
        result = integer % number
        if(result == 0):
            allDivisors.append(number)

        number -= 1
    if (len(allDivisors) == 0):
        return str(integer) + " is prime"
    for i in reversed(allDivisors):
        allDivisorsReversed.append(i)

    return allDivisorsReversed


print(divisors(14))
