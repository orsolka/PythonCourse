s = str(input())
s = s.replace(',', '')
s = s.replace(':', '')
s = s.replace('-', '')
s = s.replace('...', '')
s = s.replace(';', '')
s = s.replace('.', '')
s = s.replace('!', '')
s = s.replace('?', '')
w = s.split()
k = w[0]
for i in w[1:]:
    if len(i) < len(k):
        i = k
print(len(k))
