# 1-amaliy
# def greeting():
#     print('Good morning')
#     print('Good after')
# greeting()



# 2-amaliy
# def kattasini_aniqlash(birinchi, ikkinchi):
#     if birinchi > ikkinchi:
#         print(birinchi)
#     else:
#         print(ikkinchi)
# kattasini_aniqlash(15, 22)



# 3-amaliy
# def musbat_manfiy(son):
#     if son > 0:
#         print('Musbat son')
#     else:
#         print('Manfiy son')
# musbat_manfiy(12)



# 4-amaliy
# def juft_toq(son):
#     if son % 2 == 0:
#         return f'{son} juft son'
#     else:
#         return f'{son} toq son'
# result = juft_toq(2)
# print(result)
# result = juft_toq(7)
# print(result)



# 5-amaliy
# a = 2
# b = 10
# for num in range(a, b + 1, 2):
#     print(num)



# 6-amaliy
# def yigindi(a, b = 4):
#     return a + b
# result = yigindi(10, 2)
# print(result)



# codewars masalalari
# 1-masala
# def positive_sum(arr):
#   sum = 0
#   for number in arr:
#     if number > 0:
#       sum = sum + number
#   return sum
# example = [1,-10, -20, 7, 12]
# print(positive_sum(example))



# 2-masala
# def make_negative(number):
#   if number > 0:
#     return -number
#   else:
#     return number
# print(make_negative(1))
# print(make_negative(-5))
# print(make_negative(0))



# 3-masala
# def reverse_string(string):
#   return string[::-1]
# print(reverse_string("world"))
# print(reverse_string("word"))



# 4-masala
# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"



# 5-masala
# def number_to_string(num):
#     result = str(num)
#     return result
# num = 42
# result_string = number_to_string(num)
# print(type(result_string))



# 6-masala
# def opposite(number):
#     return -number
# result = opposite(5678)
# print(result)



# 7-masala
# def remove_char(s):
#   return s[1:-1]
# print(remove_char("hello")) # prints "ell"
# print(remove_char("python")) # prints "ytho"
# print(remove_char("aeg")) # prints ""



# 8-masala
# def repeat_str(repeat, string):
#   return repeat * string
# print(repeat_str(6, "I"))
# print(repeat_str(5, "Hello"))
# print(repeat_str(3, "a"))



# 9-masala
# def square_sum(numbers):
#   total = 0
#   for n in numbers:
#     total += n**2
#   return total
# print(square_sum([1, 2, 2]))
# print(square_sum([2,2]))
# print(square_sum([]))



# 10-masala
# def summation(num):
#   return sum(range(1, num + 1))
# print(summation(2))
# print(summation(8))
# print(summation(10))



# 11-masala
# def no_space(x):
#   return x.replace(" ", "")
# print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
# print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))
# print(no_space("8aaaaa dddd r     "))



# 12-masala
# def find_smallest_int(arr):
#   smallest = arr[0]
#   for num in arr[1:]:
#     if num < smallest:
#       smallest = num
#   return smallest
# print(find_smallest_int([34, 15, 88, 2]))
# print(find_smallest_int([34, -345, -1, 100]))



# 13-masala
# def count_sheeps(sheep):
#   count = 0
#   for sheep in sheep:
#     if sheep == True:
#       count += 1
#   return count
# print(count_sheeps([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]))



# 14-masala
# def basic_op(operator, value1, value2):
#   if operator not in "+-*/":
#     return "Invalid operator"
#   result = eval(str(value1) + operator + str(value2))
#   return result
# print(basic_op("+", 4, 7))
# print(basic_op("-", 15, 18))
# print(basic_op("*", 5, 5))
# print(basic_op("/", 49, 7))
# print(basic_op("%", 10, 3))



# 15-masala
# def litres(time):
#   water = time * 0.5
#   litres = int(water)
#   return litres
# print(litres(3))
# print(litres(6.7))
# print(litres(11.8))



# 16-masala
# def century(year):
#   century = (year // 100) + 1
#   if year % 100 == 0:
#     century -= 1
#   return century
# print(century(1705))
# print(century(1900))
# print(century(1601))
# print(century(2000))



# 17-masala
# def string_to_number(s):
#   number = int(s)
#   return number
# print(string_to_number("1234"))
# print(string_to_number("605"))
# print(string_to_number("1405"))
# print(string_to_number("-7"))



# 18-masala
# def abbrev_name(name):
#   first, last = name.split()
#   initial1 = first[0].upper()
#   initial2 = last[0].upper()
#   return initial1 + "." + initial2
# print(abbrev_name("Sam Harris"))
# print(abbrev_name("patrick feeney"))



# 19-masala
# def digitize(n):
#   return list(map(int, str(n)[::-1]))
# result = digitize(35231)
# print(result)



# 20-masala
# def is_divisible(n, x, y):
#   if n % x == 0 and n % y == 0:
#     return True
#   else:
#     return False
# print(is_divisible(3, 1, 3))
# print(is_divisible(12, 2, 6))
# print(is_divisible(100, 5, 3))
# print(is_divisible(12, 7, 5))



# 21-masala
# def greet(name):
#   return "Hello, " + name + " how are you doing today?"
# result = greet('John')
# print(result)



# 22-masala
# def find_needle(haystack):
#   index = haystack.index("needle")
#   return "found the needle at position " + str(index)
# haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# print(find_needle(haystack))



# 23-masala
# def greet():
#   return "hello world!"
# result = greet()
# print(result)



# 24-masala
# def maps(a):
#   result = []
#   for element in a:
#     result.append(element * 2)
#   return result
# example = [1, 2, 3]
# print(example)



# 25-masala
# def lovefunc(flower1, flower2):
#   if flower1 % 2 != flower2 % 2:
#     return True
#   else:
#     return False
# print(lovefunc(5, 7))
# print(lovefunc(4, 6))
# print(lovefunc(3, 9))



# 26-masala
# def boolean_to_string(b):
#   return str(b)
# print(boolean_to_string(True))
# print(boolean_to_string(False))



# 27-masala
# def paperwork(n, m):
#   if n < 0 or m < 0:
#     return 0
#   else:
#     return n * m
# print(paperwork(5, 5))
# print(paperwork(-5, 5))
# print(paperwork(10, 2))



# 28-masala
# def past(h, m, s):
#   hours_in_ms = h * 3600000
#   minutes_in_ms = m * 60000
#   seconds_in_ms = s * 1000
#   return hours_in_ms + minutes_in_ms + seconds_in_ms
# print(past(0, 1, 1))
# print(past(1, 1, 1))
# print(past(23, 59, 59))



# 29-masala
# def are_you_playing_banjo(name):
#   if name[0].lower() == "r":
#     return name + " plays banjo"
#   else:
#     return name + " does not play banjo"
# result = are_you_playing_banjo('john')
# print(result)



# 30-masala
# def find_average(numbers):
#   if not numbers:
#     return 0
#   else:
#     total = sum(numbers)
#     length = len(numbers)
#     average = total / length
#     return average