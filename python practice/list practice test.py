# l = [1,2,3,4,5]
# for i, j in enumerate(l):
#     print((i,j), end=" ")

# l1=[1,23,4]
# l2=[4,5,6,]
# add=[]
# for j in range(3)
#     add.append(l1[j]+l2[j])
#
# print(add)

# original_list=[1,2,3,4,5]
# new_list=original_list.copy()
#
# print(new_list)


# s="sneha 1234 jkil a7862 k"
# sum=0
# for i in s:
#     if isinstance(i,int):
#
#         print(i)
#         if i%2==0:
#             sum=sum+i
#
#
#             print(i)

# l=["aaa", "bbbi","ppkdsj","pkdj", "pikd", "pjshdgd"]
# l1=[]
# for item in l:
#     if len(item)%2==0:
#         l1.append(item)
#     else:
#         l1.append(item[::-1])
# print(l1)

# s="absc 2356 python 87546"
# s1=set(s)
# print(s1 )
#
# for i in s:
#     if isinstance(i,int):
#         if i%2==0:
#             print(sum(i))

def add_(a,/,*,b):
    c = a+b
    return c
res = add_(1,b=2)
print(res)















