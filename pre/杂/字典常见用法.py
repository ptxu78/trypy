# 统计词频
a = 'abcAAAd'
a = list(a)
b = {}
for i in a:
    if i in b:
        b[i] +=1
    else:
        b[i] = 1
print(b)

# get && setdefault
print(b.get("e","no"))
print(b.setdefault('e',123))
print(b.get("e","no"))

# key value
print(b.keys())
print(b.values())
print(b.items())