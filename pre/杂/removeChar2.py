def removeChar2(string, idx):
    new_string = ''
    if idx >= 0:
        for i in range(0, len(string)):
            if i == idx:
                    new_string = new_string
            else:
                    new_string += string[i]
        return new_string

    if idx < 0:
        for i in range(-len(string), 0):
            if i == idx:
                new_string = new_string
            else:
                new_string += string[i]
        return new_string

sPt = "abcdefg"
print(removeChar2(sPt, -8))