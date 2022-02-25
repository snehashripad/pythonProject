import os
path = r"C:\Users\Sneha\PycharmProjects\pythonProject\files_directory\txt_log_files\sample.txt"
#1 with open(path) as file:
#     for line in file:
#         print(line)

# 2. with open(path) as file:
#
#     for lines in reversed(list(file)):
#         print(lines)

# 3.to count the spaces in the line
# with open(path) as file:
#     count=0
#     for lines in file:
#
#         for char in lines:
#             if  char == " ":
#                 count+=1
#     # print(count)
#
#   3.1.  # without using 2 for loops for the above prg
# with open(path) as file:
#     count=0
#     for lines in file:
#         spaces = lines.count(" ")
#         count+= spaces
#     print(count)

 # 3.2.to count the num ofn vowels that are starting with vowel

# with open(path) as file:
#     count=0
#     for lines in file:
#         for words in lines.split():
#             if words[0].lower() in "aeiou":
#                 count+=1
#
#     print(count)

# 4.1.to createb a dict of word and its count pair in the given file
# from collections import defaultdict
# with open(path) as file:
#
#     d={}
#
#     for lines in file:
#         l = lines.split()
#         for word in l:
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word]+= 1
#     # print(d)

#4.2.using defaultdict

# from collections import defaultdict
# dd = defaultdict(int)
# with open(path) as file:
#     for lines in file:
#         l = lines.split()
#         for word in l:
#             dd[word]+=1
#     print(dd)

#5. wap to extract all the IP address from access-log.text file
# path = r"C:\Users\Sneha\PycharmProjects\pythonProject\files_directory\txt_log_files\access-log.txt"
# with open(path) as file:
#     l=[]
#     for lines in file:
#         l.append(lines.split()[0])
#
#
#     print(l)

# # 6.to count all the lines in the file
# with open(path) as file:
#     count=0
#     for line in file:
#         count+=1
#         print(count)

#7 to create  a dict of ip addresses and their count
# from collections import defaultdict
# with open(path) as file:
#     dd = defaultdict(int)
#     for lines in file:
#         if lines.strip():
#             dd[lines.split()[0]]+=1
#
# print(dd)

# path = r"C:\Users\Sneha\PycharmProjects\pythonProject\files_directory\files_directory\txt_log_files\sample.txt"
# with open(path)
# # 7.1 using the counter class to the above prg
# from collections import Counter
# with open(path) as file:
#     l=[]
#     for lines in file:
#         l.append(lines.split()[0])
#     ip_= Counter(l)
#     print(ip_)
#
# with open(path) as file:
#     for lines in file:
#         print(lines,len(lines))





