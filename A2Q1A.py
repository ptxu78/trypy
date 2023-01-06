import random

# inStr = input()
# fStr = inStr[:len(inStr) // 4]
# LStr = inStr[-len(inStr) // 4:]
# print(fStr + LStr)


# a = input()
# print(a * 10)
# print(a * 8)
# print(a * 6)
# print(a * 4)
# print(a * 2)

[random.randint(1,49) for i in range(6)]

def generate_mark_six():
    ranList = []
    while(len(ranList) < 6):
        ranList.append(random.randint(1,49))
    print(ranList)
