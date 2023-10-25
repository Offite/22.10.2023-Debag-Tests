# date = '2025-12-31'
# year, month, day = date.split('-')
#
# tuple = ('{}', '{}', '{}')
# print(tuple.format(day, month, year))



# sum = sum('1', '2', '3', '4', '5')
# print(sum)



# list = [1, 2, 3, 4, 5, 6]
# first_half_sum = sum(list[:len(list) // 2])
# second_half_sum = sum(list[len(list) // 2:])
#
# result = first_half_sum / second_half_sum
# print(result)



# Не понял как решать 4 задание



# def max_min_dict(numbers):
#     max_num = max(numbers)
#     min_num = min(numbers)
#
#     return {
#         'max': max_num,
#         'min': min_num
#     }



# def divisors_to_list(numbers):
#     result = []
#     for number in numbers:
#         divisors = [i for i in range(1, number + 1) if number % i == 0]
#         result.append(divisors)
#     return result
#
# numbers = [28, 30, 36, 42, 48, 54]
# result = divisors_to_list(numbers)
# for number, divisors in zip(numbers, result):
#     print(f"{number} -> {divisors}")



# import random
#
# def random_unique(n, min_val, max_val):
#     random_numbers = set()
#     while len(random_numbers) < n:
#         random_numbers.add(random.randint(min_val, max_val))
#     return random_numbers
#
# n = 10
# min_val = 1
# max_val = 20
# random_numbers = random_unique(n, min_val, max_val)
# for random_number in random_numbers:
#     print(random_number)



# import random
# from colorsys import hsv_to_rgb
#
# def get_random_color():
#     hsv = (random.randrange(5) / 5,
#            random.random(),
#            (random.random() * 0.7) + 0.3)
#     rgb = hsv_to_rgb(*hsv)
#     return "rgb({},{},{})".format(round(rgb[0] * 255), round(rgb[1] * 255), round(rgb[2] * 255))
#
# print(get_random_color())



