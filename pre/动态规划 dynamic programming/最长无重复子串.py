s = 'abcdabcbb'

c = [0] * (len(s) + 1)
dic = {}
if len(s) == 1:
    pass
for i in range(1, len(s)+1):
    las = dic.get(s[i-1], -1)
    if las == -1:
        c[i] = c[i-1] + 1
    else:
        c[i] = max(c[i-1], i-las)
    dic[s[i-1]] = i
print(c)
print(c[len(s)])
