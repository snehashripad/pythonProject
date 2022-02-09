# def list_even(start, end):
#     l =[]
#     for i in range(start, end):
#         if i%2 ==0:
#             l.append(i)
#     return l


#res = print(list_even(0,21))

# default parameter
# def list_even(end, start=0):
#     l =[]
#     for i in range(start, end):
#         if i%2 ==0:
#             l.append(i)
#     return l
#
#
# print(list_even(21))
#
# def prime_(end, start=2):
#     l=[]
#
#     for n in range(start,end+1):
#         if n>1:
#             for i in range(2,n):
#                 if n%i == 0:
#                     break
#             else:
#                 l.append(n)
#
#     return l
#
#
# print(prime_(50))

# fibonacci series
# a=0
# b=1
# i=0
# while i<=10:
#     print(a, end="  ")
#     c=a+b
#     a=b
#     b=c
#     i+=1


#variable position arguments

# def sum_(*args):
#      print(args)
#      tottal=0
#      for i in args:
#          if isinstance(args, (int, float)):
#              tottal+=1
#      return(tottal)
#
#
#
# print(sum_(2,3.4, 3))
#
# def n(*args):
#
#     count=0
#     for i in args:
#         count+=1
#     return count
#
#
# print(n(2,3,4.5,5,7))
#
# def num(*args):
#     for i in args:
#         if isinstance(i,int):
#             print(i)
#
# print(num(1,2,3,3.4,"sneha",10))

# def collection_(*args):
#     #rev_string=[]
#     for item in args:
#         if isinstance(item, str):
#             #rev_string.append(item[::-1])
#              print(item[::-1], sep=",", end=" ")
#
#
# print(collection_(10,20,30,40,"sneha","shripad","dev","dutt"))


# '''def data_(*args):
#     if len(args) > 5:
#         return "no args > 5"
#     return "no less yhan 5"
#
# print(data_(2,3,4,5,6,3))'''


# def input_(msg=0):
#     return "hai
#     return msg
#
# print(input_("hello"))

#fun to check prime or not
# def prime_(n,m=1):
#     l=[]
#     for n in range(1,n):
#         if n>1:
#             for i in range(2,n):
#                 if n%i ==0:
#                     break
#             else:
#                 l.append(n)
#     print(l)
# print(prime_(100))


#last digit of the number

# def last_digit(n):
#     s=str(n)[-1]
#     return s    # rey
#
# print(last_digit(1235))
#

# def is_fibo(num):
#     a=0
#     b=1
#     while a<=num:
#         if a == num:
#             return "fibo"
#         c=a+b
#         a=b
#         b=c
#     return "not fibo"
# print(is_fibo(5 ))

# def len_iter(*args):
#     for item in args:
#         if isinstance(item,(str,list,dict,tuple)):
#             return item,len(item)
#
#
#
# print(len_iter("string",1,2,34,"sneha"[1,2,3,4]))
#

# def factorial(n):
#     if n ==1:
#         return n
#     return n*factorial(n-1)
#

def function():
    return 1,"hai"

function()






