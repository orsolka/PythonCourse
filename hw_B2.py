t = str(input(''))
m = ''
i = 0
z = ''
while i < len(t):
    x = t[i]
    if x == 'A':
        z = 'T'
    if x == 'T':
        z = 'A'
    if x == 'C':
        z = 'G'
    if x == 'G':
        z = 'C'
    i = i+1
    m = m + z
print (m[::-1])
