# a1 = "abcdaaebdcda"
# b1 = list(set(a1))
# print(b1)
# st = ""
# i=0
# while i!=len(b1):
#     count=0
#     j=0
#     while j!= len(a1):
#         if b1[i] == a1[j]:
#             count+=1
#         j+=1
#     st = st+b1[i] + str(count)
#     i+=1
# print(st)


a1 = ["google.com","yahoo.cm"]
# i=0
# while i!=len(a1):
#     a = a1.split(".")[-1]
#     i+=1
# print(a)
#
for i in a1:
    a2 = i.split(".")
    a3 = "".join(a2[0])
    print([a3], end="")


#     a2 = a1[0].split(".")
# print(a2)