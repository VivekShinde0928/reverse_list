"""
Author  : Vivek Shinde
Date    : 03/06/2020
purpose : Practice problem solving
code    : To reverse a list by three diffrent methods

"""


print('***To reverse a list by three different methods***\n')


# user_input = input('Enter Your list :')
# print(list(user_input))

# # Method1
# Rev1 = list(user_input)
# Rev1.reverse()
# print(Rev1)

# Method2
# Rev2=list(user_input[::-1])
# print(Rev2)

# Method3      
# x = list(user_input)
Rev3 = [12, 22, 32, 42]
lst = []
length_input = len(Rev3)
for i in range(length_input-1,-1,-1):
    lst.append(Rev3[i])
print(lst)

# print(Rev3[-3])
    # print(Rev3)




