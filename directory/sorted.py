# # sort based on the len
# l = ["p","j", "c", "ruby"]
# print(sorted(l,key = len, reverse=True))
#
# #to find the longets and shortest word in sentence with their lenght



# s = "hai hello welcom to python"
# s1 = s.split()
# shortest, *rest, longest = sorted(s1, key = len)
# print((longest,len(longest)), (shortest,len(shortest)))
# #
# l= ["ruby", "python", "perl"]
# print(sorted(l,key=lambda item : len(item) // 2))


# dict sorting based on ascii

# d = {"pythpn":4,"java":3,"perl":2}
# print(sorted(d.values()))
# print(sorted(d.items(),key = lambda item : item[1]))
#
# s= "hai how hello how are you"
# s1 = s.split()
# d ={}
# for item in s1:
#     d[item]:s1.count(item)
# print(d)

l = [{"names":"ram","age":12,"class":6},{"names":"sham","age":18,"class":12},{"names":"john","age":13,"class":8}]
print(l)
print(sorted(l,key=lambda item:item[1][d[value]=key]))