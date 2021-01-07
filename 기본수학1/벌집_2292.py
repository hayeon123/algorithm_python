n = int(input())

x = 1
d = 6
cnt = 1

while x < n:
    x += d * cnt
    cnt += 1

print(cnt)
