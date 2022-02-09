# s = "hai hello how hai"
# count = 0
# d = {}
# for i in s:
#     d[i]=count
#     count+=1
# print(d)
#using comp
# s1=s.split()
# d_= {}
# for word in s1:
#     if len(word)%2==0:
#         d[word]= s1.count(word)



#
# print(d_)

# s = "python is an efficient programming language i am in python course"
# s1 = s.split()
# d = {word:len(word)  for word in (s1) if word[0] in 'aeiou'}
# print(d)
# l = {10,20,"sneha","shripad"}
# d = {index:item[::-1]  if isinstance(item,str) else item for index,item in enumerate(l)}
# print(d)

# s= "bangalore"
# d={}
# for i in s:
#     d[i] = ord(i)
# print(d)

# d = {i:ord(i) for i in s}
# print(d)
# d = {"a":1,"b":2}
# d1 = {value:key}
s = {"python","apple","flipkart"}
# set_={item for item in s}
# print(set_)

# s = "hello"
# d={}
# for char in s:
#     if char not in d:
#         d[char] = 1      d[char]+=1
# print(d)

# s ="hello universe"
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#;\
#
#
#
#
#
# '0/l;['
# ]\else:#         d[i] += 1\rint(d)


# key = input("enter the key :")
# value = int(input("enter the value :"))
# d={}
# # to add key value pair
# #d.update({key:value})
# d[key] = value
# print(d)

# d= {'a': 1, 'b': 2}
# for index, items in enumerate(d.items()):
#     print(index, items )

# \st = "bigbaazar"
# d={}
# d = {char: st.count(char) for char in st}
# print(d)
# count = 0
# for char in st:
#     d[char] = count
#     count+=1
# print(d)
# from collections import defaultdict
# string = "hello world hai universe and hai"
# li = string.split()
#
# dd = defaultdict(int)
#
# dd = {word: li.count(word) for word in li}


s = "python prg lang is very simple python lang "
li = s.split()
d ={word : len(word) for word in li}
# list_ = s.split()
# for word,
#     d[word] = len(word)
# #
print(d)




# print(dd)




