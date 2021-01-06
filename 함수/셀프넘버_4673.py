num_list = list(range(1, 10000))
for i in str(12345):
    print(i)

# def getSelfNumber(num):
#     if num >= 10000:
#         return
#
#     next_num = num
#     while num > 0:
#         next_num += num % 10
#         num //= 10
#     num_list.remove(next_num)
#     getSelfNumber(next_num)
#
#
# for i in range(1, 10000):
#     try:
#         num_list.index(i)
#         getSelfNumber(i)
#     except:
#         pass
#
# for i in num_list:
#     print(i)