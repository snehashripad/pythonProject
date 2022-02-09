num = 54129784
temp =num
rev=0
count=0
while num>0:
    rem1 = num%10

    if count%2==1:
        pass
        

    else:
        rev = rev*10+rem1

        num = num // 10
print(rev)
# while(rev>0):
#     rem = rev%10
#     count+=1
#     if count%2 ==1:
#         pass
#     else:
#         rnum =rnum*10+rem
#         rev=rev//10
# print(rnum)





