# #print the string 10 times withoput using conditional statements
# print("bangalore\n"*10)
#
# #no of digits and alphabet count
# string = "hello1234$%"
# alph_count=0
# digit_count=0
# for char in string:
#     if "a"<=char<"z" or "A"<=char<"z" :
#         alph_count
#     elif
# to create and print item and its indices in alist as key value pair
# names = ['apple', 'google','apple', 'yahoo', 'yahoo', 'gmail', 'gmail', 'gmail']
# d = {}
# for index, item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item].append(index)
# print(d)

# using default dict
# from collections import defaultdict
# names = ['apple', 'google','apple', 'yahoo', 'yahoo', 'gmail', 'gmail', 'gmail']
# dd = defaultdict(list)
# for index, item in enumerate(names):
#     dd[item] = [index]
# print(dd)

names = ['apple', 'google','apple', 'yahoo', 'yahoo', 'gmail', 'gmail', 'gmail']
dict_ = {item :[index] if item not in dict_ else dict_[item].append(index) for index, item in enumerate(names)}
print(dict_)





