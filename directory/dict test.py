# d = {'a':'hello', 'b': 100, 'c': 'world'}
# d1 = {key:value[::-1] for key,value in d.items() if isinstance(value,str)}
# print(d1)

# l = ['a','a', 'a', 'b', 'b', 'c', 'd']
# d={}
# for item in l:
#     n = l.count(item)
#     if n>1:
#         d[item] = n
# print(d)
#
# d1 = {item : l.count(item) for item in l if l.count(item)>1}
# print(d1)
#
# l = ['a', 'b']
# m = [1,2]
# d = {}
# for key in l:
#     for value in m:
#         d[key] = value
#         m.remove(value)
# print(d)

# d1 = {'a':1,'b':2}
# for key,value in enumerate(d1):
#
#     value = d1[key]
#     d1[value] = key
# print(d1)

l = [1,2,1,2,3,4,5,66,77,8,9,]
d= {}
for index, item in enumerate(l):
    if index % 2 == 0:
        d[item]=index

print(d)

