s = str(input())
t = str(input())
for i in range(len(s)):
    if s[i:].startswith(t):
        print(i+1,'\t', end = '')
