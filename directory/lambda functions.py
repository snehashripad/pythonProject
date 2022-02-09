# check the given num is even or not
# even = lambda n: n%2 ==0
#
# print(even(10))

# lambda fun to multipplyn 2 num

# print()
# multi = lambda m,n: m*n
# print(multi(2,4))


# #last element of the sequence
# last_ele = lambda sequence : sequence[-1]
# print(last_ele("sneha"))
#
# p = lambda string: string[::-1]== string
#
#print(p("madam"))

# to even in or odd in given list

# l = [1,2,34]
# e_o = lambda num: f"{num} the num is even" if num%2==0 else f"{num} the num is odd"
# res = map(e_o,l)
# print(tuple(res))

#to print the list of vowels in a list
# l = ["apple","orange", "mango", "igloo"]
# vowel = lambda string: string if string[0] in "aeiou" else "not vowel"
#
# res = map(vowel,l)
# print(tuple(res))

# to convert all the string to the uppercase using map
# l = ["APPle", "oraNGE"]
# low_str_ = lambda string : string.lower()
# res = map(low_str_, l)
# print(tuple(res))

#to len of ech word

# sent = "my world my home"
# res =  map(len,sent.split())
# print(list(res))

#list of tuples char and its ascii value pair
# word= "hai hello"
# def ord_(char):
#     return char, ord(char)
#
# res = map(ord_, word)
# print(tuple(res))
#

# a= [1,2]
# b=[2,3]
# def add_(item1, item2)
#     return item1,

# l = ["python", "odd", "even", "mad"]
# def odd_len(item):
#     if len(item) %2 != 0:
#
#         return item * 2
# odd_len = filter(odd_len, l)
#
# print(list(odd_len))

#using lambda func

# odd_len = lambda string: len(string) % 2 == 0
# res = filter(odd_len, l)
# print(list(res))

# to extract the string which strats with vowel
sent = "hai hello how are you"

# def vowel_(string):
#     if string[0] in "aeiou":
#         return string
# res = filter(vowel_, sent.split())se
# print(list(res))

# vowel = lambda string : string.lower()[0] in "aeiou"
# res = filter(vowel,sent.split())
# print(list(res))
#
#
#
# to return even values in a list
l = [10,20,30,25]
# using normal fuction
# def even(num):
#     if num%2==0:
#         return num
#
# res = filter(even,l)
# print(tuple(res))

# using lambda fuction
# even = lambda num : num % 2 == 0
#
# res = map(even, l)
# print(tuple(res))

# add the elements inside a list simultaneously
a = [1,2,3,5]
b = [5,6,7,8]
# def add_(item1,item2):
#     return item1 + item2
# res = map (add_, a,b)
# print(list(res))

#using lambda function
# add_ = lambda num1: num1+num1
# res = filter(add_,a)
# print(list(res))
#

l1 = ["sneha", "shripad"]
# def sep_list(word):
#     return [word]
#
# res = map(sep_list, l1)
# print(list(res), end="")
#
# for i in res:
#     print(res)

# to print the squares of the list elements
# l1 = [1,2,3,4,5]
# def sq(num):
#     return num*num
#
# res = map(sq, l1)
# print(list(res))

# to print the squares of the list elements if the element is of even num
l1 = [1,2,3,4,5,6,7]
def even_sq(num):
    if num[0] % 2 == 0:

        return num[1]*num[1]
res = list(map(even_sq, enumerate(l1)))
def s1(res):
    return res
print(list(filter(s1,res)))





















#

