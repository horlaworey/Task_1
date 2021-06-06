# def oddNumbers(num_list):
#     odd_list = [num for num in num_list if num % 2 != 0]
#     print(odd_list)
#
#
# random_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
#                30, 31, 32, 33, 34]
#
# oddNumbers(random_list)
# oddNumbers([2, 3, 4, 5, 6, 7])

def oddNumber(start, stop):
    odd_number_list = [num for num in range(start, stop) if num % 2 != 0]
    print(odd_number_list)


oddNumber(2, 34)

