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

# Method3       ##  pending
# x = list(user_input)
# Rev3=x
# print(Rev3)
Rev3 = [1, 2, 3, 4]
for i in Rev3:
    print (Rev3[len(Rev3)-i-1])

# print(Rev3[-3])
    # print(Rev3)




