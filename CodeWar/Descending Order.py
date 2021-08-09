# Your task is to make a function that can take any non-negative integer as an argument and
# return it with its digits in descending order. Essentially, rearrange the digits to create
# the highest possible number.
# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num):
    listNumers = []

    for x in str(num):
        listNumers.append(x)

    listNumers.sort(reverse=True)
    numberReturn = "".join(listNumers)

    return int(numberReturn)


print(descending_order(42145))

# Solução encontrada na internet
# def descending_order(num):
#    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))
#
# print(descending_order(123456789))
