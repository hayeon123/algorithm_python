list = []
for i in range(10):
    a = int(input()) % 42
    try:
        list.index(a)

    except:
        list.append(a)
print(len(list))