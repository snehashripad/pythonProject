# print 10 to 1
# def c_(end, start):
#     if end < start:
#         return
#     print(end)
#     c_(end-1, start)
#
#
# print(c_(10,1))


# def sum_(n, sum=0):
#     if n>0:
#         rem = n % 10
#         sum += rem
#
#         return sum_(n//10, sum)
#     else:
#         return sum

def sum_(n):
    if n <= 1:
        return 1
    else:
        return n + sum _(n-1)

print(sum_(4))




# print(sum_(1754))

