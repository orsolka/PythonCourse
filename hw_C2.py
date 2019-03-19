a = list(str(input()))
m = 1
print(sum((int(a[i]) for i in range(0, int(len(a))))))
for i in range(len(a)):
    m *= int(a[i])
print(m)
