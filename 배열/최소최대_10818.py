n = int(input())
k = list(map(int, input().split()))
print('{} {}'.format(min(k),max(k)))
# min = k[0]
# max = k[0]
# for i in range(1,n):
#     if k[i]<min :
#         min = k[i]
#     elif k[i]>max:
#         max = k[i]
# print(min, max)